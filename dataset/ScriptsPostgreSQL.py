import psycopg2
import os
from dotenv import load_dotenv

class ScriptsPostgreSQL:
    def __init__(self) -> None:

        super().__init__()

        load_dotenv()

        self.conn = psycopg2.connect(
            host = os.getenv('DB_PG_HOST_NAME'),
            dbname = os.getenv('DB_PG_NAME'),
            user = os.getenv('BD_PG_USER_NAME'),
            password = os.getenv('DB_PG_PASSWORD'),
            port = os.getenv('DB_PG_PORT')
        )

    def get_script_sql(self, file_name:str)->None:

        root_path = 'models'

        f = open('/'.join(["dataset", root_path, file_name]), 'rb')

        script_sql = f.read()

        f.close()

        return script_sql

    def close_connection(self)->None:
        if self.conn is not None:
            self.conn.close()

    def set_tables_in_db(self, file_name:str)->None:

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

    def delete_all_data(self)->None:
        try:
            cursor = self.conn.cursor()
            cursor.execute('DELETE FROM CONTRATO')
            cursor.execute('TRUNCATE TABLE CONTRATO RESTART IDENTITY CASCADE')
            cursor.execute('DELETE FROM NODE')
            cursor.execute('TRUNCATE TABLE NODE RESTART IDENTITY CASCADE')
            cursor.execute('DELETE FROM INFRAESTRUTURA')
            cursor.execute('TRUNCATE TABLE INFRAESTRUTURA RESTART IDENTITY CASCADE')
            cursor.execute('DELETE FROM UNIDADE_ESCOLAR')
            cursor.execute('TRUNCATE TABLE UNIDADE_ESCOLAR RESTART IDENTITY CASCADE')

            cursor.execute('DELETE FROM COLETA')
            cursor.execute('TRUNCATE TABLE COLETA RESTART IDENTITY CASCADE')
            cursor.execute('DELETE FROM ALUNO')
            cursor.execute('TRUNCATE TABLE ALUNO RESTART IDENTITY CASCADE')
            cursor.execute('DELETE FROM PROFESSOR')
            cursor.execute('TRUNCATE TABLE PROFESSOR RESTART IDENTITY CASCADE')
            self.conn.commit()
        except Exception as e:
            print(e)

    def see_n_first_rows_from(self, table_name:str, n=100)->None:
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM {} limit {}".format(table_name, n))

            rows = cursor.fetchall()

            for row in rows:
                print(row)

        except Exception as e:
            print(e)
