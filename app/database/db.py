import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from mysql.connector import IntegrityError

import sys

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='bumyyg65nr8zfnbkbkqf-mysql.services.clever-cloud.com',
            database='bumyyg65nr8zfnbkbkqf',
            user='uor0o6uchqmi5njs',
            password='zMAubiGLRKVj31hNoGhm')
        try:
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected: " + db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                return connection
        except AttributeError:
            raise AttributeError

    except Error as e:
        raise e
    except AttributeError:
        raise AttributeError




