"""data access and storage layer, resolves storage requests by resolving urls in the dataclass"""

from typing import Dict, List
from collections import OrderedDict
from commons.db_con_helper import get_sql_db_connection
from models.datamodels.characters import Character
from models.datamodels.films import Film
from pydantic.error_wrappers import ValidationError


def print_character() -> None:
    """Prints single character present in the database.
       Use this function for testing purposes.
    """
    connection = get_sql_db_connection()
    try:
        with connection.cursor() as cursor:
            # Read all the record
            sql = "SELECT * FROM starwarsDB.characters"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close()


def build_upsert_sql_query(
    table_name,
    commands,
    prime_key,
    prime_value,
    clause,
    keys_,
    values_
) -> str:
    """BUilds sql query based on input.

    Args:
        table_name (str): table under consideration for sql query.
        commands (str): sql commands such as select, insert, update etc.
        prime_key (str): primary key for particular table.
        prime_value(str): value to be updated for primary key
        clause (str): clauses to filter results.
        keys_ (list): list of keys query refers to.
        values_ (list): list of values query stores (required for insert and update statements.)

    Returns:
        query (str): complete sql query

    """

    keys_literals = ", ".join(keys_)

    mid_literals = []
    for i in range(len(values_)):
        mid = '''"''' + str(values_[i]) + '''"'''
        mid_literals.append(mid)

    values_literals = ", ".join(mid_literals)

    mid_update_literals = []
    for key_lit, val_lit in zip(keys_, mid_literals):
        mid = ''' , ''' + key_lit + '''=''' + val_lit
        mid_update_literals.append(mid)

    update_literals = "".join(mid_update_literals)

    # skipping first
    update_literals = update_literals[3:]

    sql = r"{} {}" \
          r"({}, {}) " \
          r"VALUES({}, {})" \
          r" {} {};" \
          r"".format(commands,
                     table_name,
                     prime_key,
                     keys_literals,
                     int(prime_value),
                     values_literals,
                     clause,
                     update_literals
                     )

    return sql


def get_url_ids(urls) -> str:
    """retrieves id part of singlular record urls such as "https://swapi.co/api/films/2/"

    Args:
        urls (list): list of urls

    Returns:
        str: space delimited string having ids from all urls.
    """
    ids = []
    for url in urls:
        ids.append(url.split('/')[-2])
    return ' '.join(ids)


def get_people_film_mapping() -> List:
    """
    Returns (list): All the characters present in the database.
    """
    connection = get_sql_db_connection()
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT char_id, films FROM starwarsDB.characters"
            cursor.execute(sql)
            result = cursor.fetchall()
            # print(f"FUNCTION get_people_film_mapping() - {result}")
            return result
    finally:
        connection.close()


def upsert_characters(character: Dict, endpoint: str) -> None:
    """
    Inserts values into `characters` table, updates on duplicate key.
    Args:
        character (dict):
        endpoint (str):
    Returns:

    """

    connection = get_sql_db_connection()

    # retrieving keys and values from an OrderedDict into list so as to maintain relative order
    character = OrderedDict(character)

    char_id = get_url_ids([endpoint])
    keys_ = []
    values_ = []
    for key_, val_ in character.items():
        keys_.append(key_)
        if isinstance(val_, list):
            values_.append(get_url_ids(val_))
        else:
            values_.append(val_)

    # data validation layer using pydantic model. If endpoint yields no result then return.
    try:
        if character is not OrderedDict([('detail', 'Not found')]):
            Character(**character)
        else:
            print(f"\n\n[ WARNING ] Endpoint - {endpoint} - yields nothing!!")
            return None
    except ValidationError as ve:
        print(f"[ Error ] fetched character record does not meet validations. Perhaps, type"
              f"conversions required. More details on error  - {ve}")

    try:
        with connection.cursor() as cursor:

            sql = build_upsert_sql_query(
                "starwarsDB.characters",
                "INSERT INTO",
                "char_id",
                char_id,
                "ON DUPLICATE KEY UPDATE",
                keys_,
                values_
            )

            # print(f"\n see here the SQL query :: \n\n{sql}")

            cursor.execute(sql)
            connection.commit()
    finally:
        connection.close()


def upsert_films(film: Dict, endpoint: str) -> None:
    """
    Inserts values into `films` table, updates on duplicate key.
    Args:
        film (dict):
        endpoint (str):
    Returns:

    """

    connection = get_sql_db_connection()

    # retrieving keys and values from an OrderedDict into list so as to maintain relative order
    character = OrderedDict(film)

    film_id = get_url_ids([endpoint])
    keys_ = []
    values_ = []
    for key_, val_ in film.items():
        keys_.append(key_)
        if isinstance(val_, list):
            values_.append(get_url_ids(val_))
        else:
            values_.append(val_)

    try:
        Film(**film)
    except ValidationError as ve:
        print(f"[ Error ] fetched character record does not meet validations. Perhaps, type"
              f"conversions required. More details on error  - {ve}")

    try:
        with connection.cursor() as cursor:

            sql = build_upsert_sql_query(
                "starwarsDB.film",
                "INSERT INTO",
                "film_id",
                film_id,
                "ON DUPLICATE KEY UPDATE",
                keys_,
                values_
            )

            # print(f"\n see here the SQL query :: \n\n{sql}")

            cursor.execute(sql)
            connection.commit()
    finally:
        connection.close()


def upsert_people_film_rels(mapping: Dict) -> None:
    """
    Inserts values into `CharFilmRelation` table, updates on duplicate key.
    Args:
        mapping (dict):
    Returns:
    """

    connection = get_sql_db_connection()
    try:
        with connection.cursor() as cursor:
            for key_ in mapping.keys():
                for val_ in mapping[key_]:
                    sql = r"INSERT INTO " \
                          r"CharFilmRelation(char_id, film_id)" \
                          r" VALUES({}, {})" \
                          r" ON DUPLICATE KEY UPDATE char_id={}, film_id={}" \
                          r";".format(key_, val_, key_, val_)

                    cursor.execute(sql)
                    connection.commit()
    finally:
        connection.close()


def format_output(people_id) -> Dict:
    """

    Args:
        people_id (int): user selected character id for which results to be displayed

    Returns:
        dict formatted result
    """
    connection = get_sql_db_connection()
    try:
        with connection.cursor() as cursor:
            sql1 = r" SELECT starwarsDB.characters.name, " \
                   r"starwarsDB.characters.homeworld, " \
                   r"starwarsDB.characters.gender " \
                   r"FROM starwarsDB.characters " \
                   r"where starwarsDB.characters.char_id={};".format(people_id)

            cursor.execute(sql1)
            sql1_result = cursor.fetchall()

            sql2 = r"SELECT starwarsDB.film.title " \
                   r"FROM starwarsDB.film " \
                   r"INNER JOIN starwarsDB.CharFilmRelation " \
                   r"ON starwarsDB.film.film_id = starwarsDB.CharFilmRelation.film_id " \
                   r"WHERE starwarsDB.CharFilmRelation.film_id " \
                   r"IN" \
                   r" (select starwarsDB.CharFilmRelation.film_id " \
                   r"FROM starwarsDB.CharFilmRelation " \
                   r"WHERE starwarsDB.CharFilmRelation.char_id = {});".format(people_id)
            cursor.execute(sql2)
            sql2_result = cursor.fetchall()

            unique_movies = list(set([v['title'] for v in sql2_result]))

            final_result = []
            for movie in unique_movies:
                mid_result = {}
                mid_result.setdefault("film", movie)
                mid_result.setdefault("characters", [])
                mid_result["characters"].extend(sql1_result)
                final_result.append(mid_result)

            return final_result

    finally:
        connection.close()
