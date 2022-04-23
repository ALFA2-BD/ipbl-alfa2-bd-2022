from distutils.debug import DEBUG
import psycopg2
import os
from dotenv import load_dotenv

class ScriptsSql:
    def __init__(self) -> None:

        super().__init__()

        load_dotenv()

        self.conn = psycopg2.connect(
            host = os.getenv('HOST_NAME'),
            dbname = os.getenv('DB_NAME'),
            user = os.getenv('USER_NAME'),
            password = os.getenv('PASSWORD'),
            port = os.getenv('PORT')
        )

    def get_script_sql(self, file_name):

        root_path = 'models'

        f = open('/'.join(["dataset", root_path, file_name]), 'rb')

        script_sql = f.read()

        f.close()

        return script_sql

    def close_connection(self):
        if self.conn is not None:
            self.conn.close()

    def set_tables_in_db(self, file_name:str):

        script_sql = self.get_script_sql(file_name)

        try:
            cursor = self.conn.cursor()
            cursor.execute(script_sql)
            self.conn.commit()

        except Exception as e:
            print(e)
        finally:
            if cursor is not None:
                cursor.close()

    def delete_all_data(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('DELETE FROM INFRAESTRUTURA')
            cursor.execute('DELETE FROM UNIDADE_ESCOLAR')
            cursor.execute('DELETE FROM CONTRATO')
            cursor.execute('DELETE FROM NODE')
            self.conn.commit()
        except Exception as e:
            print(e)