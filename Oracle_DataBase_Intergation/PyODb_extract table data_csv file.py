import cx_Oracle
import pandas as pd

cx_Oracle.init_oracle_client(lib_dir=r"C:\Oracle\instantclient_21_3")

con = cx_Oracle.connect('TRAINEE19/TRAINEE19@//192.168.0.99:1521/rmclient')
sql_query = pd.read_sql_query('''SELECT * FROM CEO_DETAILS''', con)
print(sql_query)
# sql_query.to_csv('sql_data_export_CEO.csv', index=False)