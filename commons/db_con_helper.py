# -*- coding: utf-8 -*-

"""
This module defines utility to connect with database.
"""
import os
import yaml

import pymysql
from pymysql.connections import Connection

_settings = {}


def _load_from_file(filename):
    """Loads settings from a YAML file and stores them under the ``_settings``
    global variable

    Args:
        filename (str): The filename of the YAML file containing the settings.
    """

    global _settings

    if not os.path.exists(filename):
        return

    with open(filename, 'r') as f:
        doc = yaml.load(f)

    if not doc:
        return

    for k, v in doc.items():
        _settings[k] = v


def _abs_path(filename):
    """Returns the absolute path to the provided ``filename``.

    Args:
        filename (str): The filename for which the absolute path will be
            assembled.

    Returns:
        str: The assembled absolute path for ``filename``.
    """
    return os.path.join(os.path.dirname(__file__), filename)


def _load():
    """Loads the settings YAML files and stores their content under the
    ``_settings`` variable.

    Note:
        Settings under ``settings/secrets.yaml`` are only loaded in a DEV
        environment.

    """

    global _settings

    env_filename = _abs_path('settings/secrets.yaml')
    _load_from_file(env_filename)


def get_sql_db_connection() -> Connection:
    """ Assembles connection object to the SQL database.

    Returns:
        Connection:  connection object to the SQL database.
    """

    _load()
    global _settings

    sql_username = _settings.get("LOCALSQL_USER")
    sql_password = _settings.get("LOCALSQL_PASSWORD")
    sql_host = _settings.get("LOCALSQL_HOST") or ""
    sql_port = _settings.get("LOCALSQL_PORT")
    sql_db = _settings.get("LOCALSQL_DATABASE")

    connection = pymysql.connect(host=sql_host,
                                 user=sql_username,
                                 password=sql_password,
                                 db=sql_db,
                                 port=sql_port,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    return connection
