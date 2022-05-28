from dataset.ScriptsSql import ScriptsSql
import os

sql_scripts = ScriptsSql()

sql_scripts.set_tables_in_db('modelo_aluno_professor.sql')
sql_scripts.set_tables_in_db('modelo_escola_infraestrutura.sql')

sql_scripts.close_connection()