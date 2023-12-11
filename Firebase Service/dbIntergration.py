from sqlite3 import Error
from firebase import firebase
import sqlite3
import time

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_task_by_priority(conn, priority):
    #print(type(priority))
    prioritystring=int(priority)
    #print(type(prioritystring))
    c = conn.cursor()
    c.execute("SELECT * FROM trackingsystem_student WHERE fingerprintID=?", (prioritystring,))
    #c.execute("SELECT fingerprintID FROM trackingsystem_student")
    #c.execute("SELECT * FROM trackingsystem_student WHERE fingerprintID=5")

    rows = c.fetchall()
    #print(rows)
    stateHere = rows[0][5]
    print("asdad")
    print(stateHere)
    #print(type(stateHere))


    for row in rows:
        print("row")
        print(row)

    if (stateHere == "1"):
        #c.execute("UPDATE trackingsystem_student SET state=0 WHERE fingerprintID='5'")
        c.execute("UPDATE trackingsystem_student SET state=0 WHERE fingerprintID=?", (prioritystring,))
    else:
        #c.execute("UPDATE trackingsystem_student SET state=1 WHERE fingerprintID='5'")
        c.execute("UPDATE trackingsystem_student SET state=1 WHERE fingerprintID=?", (prioritystring,))

    c.execute("SELECT * FROM trackingsystem_student WHERE fingerprintID=?", (priority,))
    print("fetch")
    print(c.fetchall())


def firebasedef(result):
    abc = result
    database = r"C:\Users\Lenovo\Desktop\Fingerprint Project\firebase_webserver\db.sqlite3"

    conn = create_connection(database)

    with conn:
        select_task_by_priority(conn, abc)
        # select_all_tasks(conn)

    conn.commit()
    conn.close()


def main():

    while (1):
        time.sleep(1)
        result = firebase.get('/fingerID', None)
        if (result != -1):
            print(result)
            firebasedef(result)


if __name__ == '__main__':
    firebase = firebase.FirebaseApplication('https://pythonfirebaselora.firebaseio.com/', None)
    main()