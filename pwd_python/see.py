"Module for seeing the entirety of the db"
import sys
import traceback
from mysql.connector import connect, Error
from colr import color
import fire
from db_decorator.db_information import db_information


@db_information
def see():
    try:
        conn = connect(
            host = "localhost",
            user = "mic",
            password = "xxxx",
            database = "pwd")
        cur = conn.cursor()
        query = """ SELECT * FROM pwd """
        cur.execute(query)
        records = cur.fetchall()
        for row in records:
            print(color(' [0] ID » ', fore='#3c828e'), color(str(row[0]), fore='#efb666'))
            print(color(' [1] SITE » ', fore='#3c828e'), color(str(row[1]), fore='#efb666'))
            print(color(' [2] USERNAME » ', fore='#3c828e'), color(str(row[2]), fore='#efb666'))
            print(color(' [3] PASSWORD » ', fore='#3c828e'), color(str(row[3]), fore='#efb666'))
            print(color(' [4] COMMENT » ', fore='#3c828e'), color(str(row[4]), fore='#efb666'))
            print(color(' [5] TIME » ', fore='#3c828e'), color(str(row[5]), fore='#efb666'))
            print('\n')
    except Error as e:
        print("Error while connecting to db", e)
        print("Exception class is: ", e.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    finally:
        if(conn):
            conn.close()


if __name__ == '__main__':
    fire.Fire(see)
