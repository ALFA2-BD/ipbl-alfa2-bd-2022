import psycopg2
import os
from dotenv import load_dotenv

def get_script_sql(file_name):

    root_path = 'scripts_sql'

    f = open('/'.join([root_path, file_name]), 'rb')

    script_sql = f.read()

    f.close()

    return script_sql


if __name__ == '__main__':

    script_sql = get_script_sql('modelo_escola_infraestrutura.sql')

    load_dotenv()

    HOST_NAME = os.getenv('HOST_NAME')
    DB_NAME = os.getenv('DB_NAME')
    USER_NAME = os.getenv('USER_NAME')
    PASSWORD = os.getenv('PASSWORD')
    PORT = os.getenv('PORT')

    try:

        conn = psycopg2.connect(
            host = HOST_NAME,
            dbname = DB_NAME,
            user = USER_NAME,
            password = PASSWORD,
            port = PORT
        )

        cursor = conn.cursor()
        cursor.execute(script_sql)

    except Exception as e:
        print(e)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()