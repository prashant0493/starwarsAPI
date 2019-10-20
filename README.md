# Introduction

The project contains two tasks that pull data off [starwar API](https://swapi.co) and stores into 
MySQL database using dal (data access layer).

# Setup
Create virtualenv

```
virtualenv venv
```
Activate virtualenv

```
source venv/bin/activate
```

Install dependencies (using virtual environment is recommended):
```
pip install -r requirements.txt
```

`mysql` database installation - 
This project has been tested against `mysql-5.6.47` using `OSX` native package installation. More
instructions [here](https://dev.mysql.com/doc/refman/5.6/en/osx-installation-pkg.html) 

Provide MySQL credentials in `config/secrets.yaml`:
```
# ---LOCAL---
LOCALSQL_USER: root
LOCALSQL_HOST: 127.0.0.1
LOCALSQL_PORT: 3306
LOCALSQL_PASSWORD: xxxxx
LOCALSQL_DATABASE: starwarsDB
```

`pymysql` [installation](https://pymysql.readthedocs.io/en/latest/user/installation.html) and 
related versions of `mysql` should be matched.

# Usage
Activate virtual env `source venv/bin/activate`
Start the app with `python task_one.py`

Good luck!

# Running tests

[TODO] to be added soon.

# Development notes


    The database modeling for the starwars API goes like follows: 
    Name of models -
    
    characters (aka people)    
    film          
    species                   
    vehicle                   
    planets                   
    starships                 
    
    sql script establishes ``many-to-many`` with `characters` and `film` table with other tables.
    
    For example,
    
    people (aka characters) <--->   film      :: many-to-many
    people                  <--->   species   :: many-to-many 
    people                  <--->   vehicles  :: many-to-many
    people                  <--->   planets   :: many-to-many
    people                  <--->   starships :: many-to-many
    
    [TODO] More description to be added here.
    
    INSTRUCTIONS
    
    [1] To setup, database use sql script `database_.sql` (contains DDL).
    [2] You should have `settings/secrets.yaml` for database credentials
    
    Example, 
    ```
    # ---LOCAL---
    LOCALSQL_USER: root
    LOCALSQL_HOST: 127.0.0.1
    LOCALSQL_PORT: 3306
    LOCALSQL_PASSWORD: xxxx
    LOCALSQL_DATABASE: starwarsDB
    ```

# coding style

[1] Since the code has been written in Python3.7, function annotations and type-hinting has been  
    used across.
[2] Google-Styled docstrings have been used to describe functions/classes/modules.
[3] Pydantic data-classes have been used to validate the responses from starwar API endpoints.
[4] Set your IDE character limit per line to maximum 100 (recommendation)
[5] Set your configurations via ``settings/secrets.yaml``; Do *NOT* commit file containing secrets.
[6] The generic functionality has been maintained under ``commons``.
    
# Task 1

    The Star Wars API lists 87 main characters in the Star Wars saga. For the first task, we would
    like you to use a random number generator that picks a number between 1-87. Using these
    random numbers you will be pulling 15 characters from the API using Python.
    
# Notes

Random number generator may produce some integers IDs within `range(1, 87)` which may not yield any
results from starwars API (404s). In which case, we skip those IDs and store the rest (fair enough?)


# Future scopes

    The task involves lot of IO-bound operations. Support for multi-theading based fetch is to be 
    added.
    
    ** [TODO] try another approach ** - 
    
    Crawl through all the urls from starwars API first, resolve dependecies endpoint-by-endpoint 
    and store into record tables and relationship tables.
    Finally, use local database to produce results per ask in the task.
                       
    
