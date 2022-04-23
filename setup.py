from dataset.ScriptsSql import ScriptsSql
import os

sql_scripts = ScriptsSql()
sql_scripts.set_tables_in_db('modelo_escola_infraestrutura.sql')

os.system('pip install -r requirements.txt')