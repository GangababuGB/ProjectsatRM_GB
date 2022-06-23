import cx_Oracle
import pandas as pd

cx_Oracle.init_oracle_client(lib_dir=r"C:\Oracle\instantclient_21_3")
# con = cx_Oracle.connect('TRAINEE19/TRAINEE19@//192.168.0.99:1521/rmclient')

# # Step 1. Prepare or identify your data
irisData = pd.read_csv('https://github.com/Muhd-Shahid/Write-Raw-File-into-Database-Server/raw/main/iris.csv', index_col=False)
print(irisData.head())
print(irisData.info())

# # Step 2. Connect to the Oracle and create a table
from cx_Oracle import DatabaseError

try:
    conn = cx_Oracle.connect('TRAINEE19/TRAINEE19@//192.168.0.99:1521/rmclient')
    if conn:
        print("cx_Oracle version:", cx_Oracle.version)
        print("Database version:", conn.version)
        print("Client version:", cx_Oracle.clientversion())

        # Now execute the sqlquery
        cursor = conn.cursor()
        print("You're connected.................")

        # Drop table if exists
        print('Droping iris table if exists............')
        cursor.execute("BEGIN EXECUTE IMMEDIATE 'DROP TABLE iris'; EXCEPTION WHEN OTHERS THEN NULL; END;")

        print('Creating table iris............')
        cursor.execute(
            "CREATE TABLE iris (sepal_length number(3,1) NOT NULL, "
            "sepal_width number(3,1) NOT NULL, "
            "petal_length number(3,1) NOT NULL, "
            "petal_width number(3,1),"
            "species varchar2(10) NOT NULL)")
        print("iris table is created..............")
except DatabaseError as e:
    err, = e.args
    print("Oracle-Error-Code:", err.code)
    print("Oracle-Error-Message:", err.message)
finally:
    cursor.close()
    conn.close()

# # Step 3. Import the CSV data into the Oracle database

import cx_Oracle
from cx_Oracle import DatabaseError
try:
    conn = cx_Oracle.connect('TRAINEE19/TRAINEE19@//192.168.0.99:1521/rmclient')
    if conn:
        print("cx_Oracle version:", cx_Oracle.version)
        print("Database version:", conn.version)
        print("Client version:", cx_Oracle.clientversion())
        cursor = conn.cursor()
        print("You're connected: ")
        print('Inserting data into table....')
        for i, row in irisData.iterrows():
            sql = "INSERT INTO iris(sepal_length,sepal_width,petal_length,petal_width,species) VALUES(:1,:2,:3,:4,:5)"
            cursor.execute(sql, tuple(row))
        # the connection is not autocommitted by default, so we must commit to save our changes
        conn.commit()
        print("Record Inserted Successfully.")
except DatabaseError as e:
    err, = e.args
    print("Oracle-Error-Code:", err.code)
    print("Oracle-Error-Message:", err.message)
finally:
    cursor.close()
    conn.close()

# # 3.1.1. Query the database to check our work

conn = cx_Oracle.connect('TRAINEE19/TRAINEE19@//192.168.0.99:1521/rmclient')
cursor = conn.cursor()
# Execute query
sql = "SELECT * FROM iris"
cursor.execute(sql)
# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)

cursor.close()
conn.close()

