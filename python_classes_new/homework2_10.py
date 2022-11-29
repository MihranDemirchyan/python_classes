import sqlite3
from sqlite3 import Error
import os
import sys
import json
import pprint

database = os.path.join(os.getcwd(), "database/film_data.db")
print(database)

conn = sqlite3.connect(database)

try:
    curs = conn.cursor()
except Error as err:
    print(err)
    sys.exit()

# EX_1
name_start = """SELECT title
                FROM film_data
                WHERE title LIKE "B%"
"""

result = curs.execute(name_start)
pprint.pprint(result.fetchall())

# EX_2
film_duration = """SELECT *
                    FROM film_data
                    ORDER by length desc"""

result_1 = curs.execute(film_duration)
pprint.pprint(result_1.fetchone())

# # EX_3




# # EXTRA

films_table = """CREATE TABLE IF NOT EXISTS films (
                    id integer PRIMARY KEY,
                    film_name text,
                    release_y integer
                    ); """
# curs.execute(films_table)
# conn.commit()


table_insert = """INSERT INTO films
                    SELECT film_id, title, release_year
                    FROM film_data
                    WHERE release_year > 2010 
                    """
curs.execute(table_insert)
conn.commit()



