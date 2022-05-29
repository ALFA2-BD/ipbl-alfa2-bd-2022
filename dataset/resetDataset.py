from dataset.ScriptsPostgreSQL import ScriptsSql

sql_scripts = ScriptsSql()

sql_scripts.get_script_sql('modelo_aluno_professor.sql')
sql_scripts.get_script_sql('modelo_escola_infraestrutura.sql')

sql_scripts.delete_all_data()
sql_scripts.close_connection()