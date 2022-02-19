import sys
import traceback
from mysql.connector import connect, Error
from colr import color
import fire


def search_int():
    try:
        busca = input(color(' What is the id? ', fore='#fe7243'))
        conn = connect(
                host="localhost",
                user="mic",
                password="xxxx",
                database="pwd")
        cur = conn.cursor()
        query = " SELECT pwdid, site, username, passwd, comment, time FROM pwd WHERE pwdid = " + busca
        cur.execute(query)
        records = cur.fetchall()
        for row in records:
            print(color(' [0] ID » ', fore='#3c828e'), color(str(row[0]), fore='#efb666'))
            print(color(' [1] SITE » ', fore='#3c828e'), color(str(row[1]), fore='#efb666'))
            print(color(' [2] USERNAME » ', fore='#3c828e'), color(str(row[2]), fore='#efb666'))
            print(color(' [3] PASSWORD » ', fore='#3c828e'), color(str(row[3]), fore='#efb666'))
            print(color(' [4] COMMENT » ', fore='#3c828e'), color(str(row[4]), fore='#efb666'))
            print(color(' [5] TIME : ', fore='#3c828e'), color(str(row[5]), fore='#efb666'))
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
    fire.Fire(search_int)
