import cx_Oracle
import pandas as pd

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
        data = cur.fetchall()
        Q = cur.execute(sql_fetch)
        col = []
        for column in Q.description:
            col.append(column[0])
        df = pd.DataFrame(data)
        df.columns = col
        print(df)
        df.to_csv('ceo_data.csv') #index=False,
        print('Table saved as CSV.')
    except Exception as err:
        print('Exception occurred while fetching the record', err)
    else:
        print('Fetched.')
    finally:
        cur.close()
finally:
    con.close()