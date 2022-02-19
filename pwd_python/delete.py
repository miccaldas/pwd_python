""" Here we create a function to allow the user to delete a entry in the app """
import sys
import traceback
from mysql.connector import connect, Error
from colr import color


def delete():
    ident = input(color(' ID to delete? » ', fore='#fe7243'))

    try:
        conn = connect(
                        host="localhost",
                        user="mic",
                        password="xxxx",
                        database="pwd")
        cur = conn.cursor()
        query = " DELETE FROM pwd WHERE pwdid = " + ident
        cur.execute(query)
        conn.commit()

    except Error as e:
        print("Error while connecting to db", e)
        print('SQLite error: %s' % (' '.join(e.args)))
        print("Exception class is: ", e.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    finally:
        if(conn):
            conn.close()


if __name__ == '__main__':
    delete()
