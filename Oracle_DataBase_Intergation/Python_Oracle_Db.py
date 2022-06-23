import cx_Oracle
# import requests
# import flask

cx_Oracle.init_oracle_client(lib_dir=r"C:\Oracle\instantclient_21_3")

# cx_Oracle.init_oracle_client(lib_dir=r"C:\Oracle\instantclient_21_3")
# con = cx_Oracle.connect('TRAINEE19/TRAINEE19@//192.168.0.99:1521/rmclient')
# print(con.version)

# cur = con.cursor()

# sql_create = """
# CREATE TABLE CEO_DETAILS(
#     FIRST_NAME VARCHAR2(50),
#     LAST_NAME VARCHAR2(50),
#     COMPANY VARCHAR(50),
#     AGE NUMBER
# )
# """

# cur.execute(sql_create)
# print('Table Created.')

try:
    # Create connection
    con = cx_Oracle.connect('TRAINEE19/TRAINEE19@//192.168.0.99:1521/rmclient')
except Exception as err:
    print('Error while creating the connection ', err)
else:
    print(con.version)
    try:
        # create cursor
        cur = con.cursor()
        sql_insert = """ 
        INSERT INTO CEO_DETAILS VALUES (:1, :2, :3, :4, :5)
        """
        data = [('Sundar', 'Pichai', 'Google', 47, 1), ('Mark', 'Zuck', 'Meta', 45, 2),
                ('Kabilan', 'S', 'RoadmapIT', 54, 3), ('Steve', 'Jobs', 'Apple', 64, 4)]
        cur.executemany(sql_insert, data)
    except Exception as err:
        print('Error while inserting the data', err)
    else:
        print('Table Insert completed.')
        con.commit()
finally:
    cur.close()
    con.close()


