import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"C:\Oracle\instantclient_21_3")

try:
    con = cx_Oracle.connect('TRAINEE19/TRAINEE19@//192.168.0.99:1521/rmclient')
except Exception as err:
    print('Error while creating the connection ', err)
else:
    try:
        cur = con.cursor()
        sql_fetch = """
        SELECT * FROM CEO_DETAILS
        """
        cur.execute(sql_fetch)
        data = cur.fetchmany(3)
        print(data)

        # for index, record in enumerate(data_r1):
        #     print('Index ', index, ' : ', record)
    except Exception as err:
        print('Exception occurred while fetching the record', err)
    else:
        print('Fetched.')
    finally:
        cur.close()
finally:
    con.close()