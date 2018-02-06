import sys
import time
import random

import MySQLdb
import _mysql_exceptions

DB_HOST = ""
DB_PORT = 3306
DB_USERNAME = ""
DB_PASSWORD = ""
DB_DATABASE = ""


def insert_data(temperature):
    try:
        db = MySQLdb.connect(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_DATABASE)
    except _mysql_exceptions.OperationalError as e:
        print "Connection fails"
        sys.exit("Connection fails!")

    sql = "INSERT INTO data VALUES (null, {temp}, NOW())".format(temp=temperature);
    cursor = db.cursor()

    try:
        cursor.execute(sql)
        db.commit()
    except:
        print "Insert sql fails"
        db.rollback()
    finally:
        db.close()


if __name__ == '__main__':
    while True:
        randint = random.randint(275, 280)
        insert_data(randint)
        time.sleep(3)
