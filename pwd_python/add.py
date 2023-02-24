""" This modules pertains to the insertion of new entries into the password db."""
import random
from mysql.connector import connect, Error
from colr import color
import fire
from tabulate import tabulate
from db_decorator.db_information import db_information


@db_information
def add():
    """Here we'll be doing two things. Which means that what I have here in reality are two functions. But I just can't be bothered. Here we'll
    promt the user for the data for a new entry. After that we'll check if there is already a site with the same name in the db. If true,
    we'll ask the user if want's to continue; if no, the function ends, if yes, it continues to the rest of function, that consists in sending
    the data inputed into the db and printing this data."""

    a = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "0",
        "A",
        "a",
        "B",
        "b",
        "C",
        "c",
        "D",
        "d",
        "E",
        "e",
        "F",
        "f",
        "G",
        "g",
        "H",
        "h",
        "I",
        "i",
        "J",
        "j",
        "K",
        "k",
        "L",
        "l",
        "M",
        "m",
        "N",
        "n",
        "O",
        "o",
        "P",
        "p",
        "Q",
        "q",
        "R",
        "r",
        "S",
        "s",
        "T",
        "t",
        "U",
        "u",
        "V",
        "v",
        "W",
        "w",
        "X",
        "x",
        "Y",
        "y",
        "Z",
        "z",
        "|",
        "!",
        '"',
        "#",
        "$",
        "%",
        "&",
        "/",
        "(",
        ")",
        "=",
        "«",
        "^",
        "<",
        ">",
        "[",
        "}",
        "+",
        "*",
        "ç",
        "`",
        "~",
        "_",
        "-",
        ".",
        ";",
        "|",
    ]

    try:
        print("\n")
        sitio = input(color("  [*] What is the name of the site? ", fore="#fe7243"))
        username = input(color("  [*] What is the username? ", fore="#fe7243"))
        k = int(input(color("  [*] How long do you want your password to be? ", fore="#fe7243")))
        author = input(color("  [*] Do you want to name the password yourself? [y/n] ", fore="#fe7243"))
        comment = input(color("  [*] Any comments you would like to add? ", fore="#fe7243"))
        if author == "y":
            passwd = input(color("  [*] What name do you want to use? ", fore="#fe7243"))
        else:
            pass
        passwd = str("".join(random.sample(a, k)))
        answers = [sitio, username, passwd, comment]

        conn = connect(host="localhost", user="mic", password="xxxx", database="pwd")
        cur = conn.cursor()

        # With query1 we are checking if there is another site by the inputed.
        query1 = "SELECT * FROM pwd WHERE site LIKE %s"
        cur.execute(query1, (sitio,))
        records = cur.fetchall()
        # We transform records in a list, because we want to use a 'if ... in ...' expression, which is used in iterables only.
        records = list(records)
        for row in records:
            # Here is what we were talking about in the last comment
            if sitio in row:
                print(
                    color("  WARNING - ", fore="#fe7243"),
                    color("  For the site name that you gave us, we have the following records:", fore="#fe7243"),
                )
                print("\n")
                print(color("    Site - ", fore="#fe7243"), color(row[1], fore="#efb666"))
                print(color("    Username - ", fore="#fe7243"), color(row[2], fore="#efb666"))
                print(color("    Password - ", fore="#fe7243"), color(row[3], fore="#efb666"))
                print(color("    Comment - ", fore="#fe7243"), color(row[4], fore="#efb666"))
                print("\n")
                dec = input(color("  Do you want to continue inserting this record? [y/n] ", fore="#fe7243"))
                print("\n")
                if dec == "n":
                    break
                if dec == "y":
                    pass
                else:
                    print(
                        color(
                            'Oh, I see, you must be one of those challenged kids. Just a "y" or a "n" sweetie...',
                            fore="#fe7243",
                        )
                    )

        # query2 does the tradicional work for a 'add' function.
        query2 = """ INSERT INTO pwd (site, username, passwd, comment) VALUES (%s, %s, %s, %s) """
        cur.execute(query2, answers)
        conn.commit()
        conn.close()
    except Error as e:
        print("Error while connecting to db", e)

    # And finally we print the inputed data, so the user can verify the information added to the db.
    print("\n")
    # This particular format is to use tabulate. https://pypi.org/project/tabulate/
    # Tabulate only accepts a list of lists or dictionaries. To work you have to add the headers as the first element on list.
    # It shouldn't be necessary to do this, but it was the only way I could make it work
    teste = [["site", "username", "pwd", "note"], answers]
    print(tabulate(teste, headers="firstrow", tablefmt="fancy_grid"))
    print("\n")


if __name__ == "__main__":
    fire.Fire(add)
