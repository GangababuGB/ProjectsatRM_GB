import cx_Oracle
import pandas as pd

cx_Oracle.init_oracle_client(lib_dir=r"C:\Oracle\instantclient_21_3")

# # Execute the below FUNCTION in SQL DB/ Query of the TABLE
# # ----------------------------------------------------------
# CREATE OR REPLACE FUNCTION ADD_INT (F_NUM1 NUMBER, F_NUM2 NUMBER)
# RETURN NUMBER
# IS
# BEGIN
#   RETURN F_NUM1 + F_NUM2;
# END;
# /

try:
    con = cx_Oracle.connect('TRAINEE19/TRAINEE19@//192.168.0.99:1521/rmclient')
except Exception as err:
    print('Error while creating the connection ', err)
else:
    try:
        cur = con.cursor()
        data = [10, 11]
        result = cur.callfunc('ADD_INT', int, data)
    except Exception as err:
        print('Exception occurred while executing the function.', err)
    else:
        print('Result : ', result)
        # print('Procedure INS_CEO_DETAILS executed.')
    finally:
        cur.close()
finally:
    con.close()