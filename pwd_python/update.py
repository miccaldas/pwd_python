""" Module to update passwords to database """
import sys
import traceback
from mysql.connector import connect, Error
from colr import color


def update():
    coluna = input(color('    Column? » ', fore='#fe7243'))
    ident = input(color('    ID? » ', fore='#fe7243'))
    update = input(color('    Write your update: ', fore='#fe7243'))

    try:
        conn = connect(
                host="localhost",
                user="mic",
                password="xxxx",
                database="pwd")
        cur = conn.cursor()
        query = " UPDATE pwd SET " + coluna + " = '" + update + "' WHERE pwdid = " + ident
        cur.execute(query)
        conn.commit()
    except Error as e:
        print("Error while connecting to db", e)
        print('MySQL error: %s' % (' '.join(e.args)))
        print("Exception class is: ", e.__class__)
        print('MySQL traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    finally:
        if(conn):
            conn.close()


if __name__ == '__main__':
    update()
