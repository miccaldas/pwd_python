import sys
import traceback
from mysql.connector import connect, Error
from colr import color
from tabulate import tabulate
import fire


def search():
    try:
        busca = input(color(' What are you searching for? ', fore='#fe7243'))
        conn = connect(
                host="localhost",
                user="mic",
                password="xxxx",
                database="pwd")
        cur = conn.cursor()
        query = " SELECT pwdid, site, username, passwd, comment, time FROM pwd WHERE MATCH(site, username, comment) AGAINST ('" \
                + busca + "' IN NATURAL LANGUAGE MODE)"
        cur.execute(query)
        records = cur.fetchall()
        headers = ['id', 'site', 'user', 'pwd', 'note', 'timestamp']
        print(tabulate(records, headers, tablefmt='fancy_grid'))
    except Error as e:
        print("Error while connecting to db", e)
        print("Exception class is: ", e.__class__)
        print('MySQL traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    finally:
        if(conn):
            conn.close()


if __name__ == '__main__':
    fire.Fire(search)
