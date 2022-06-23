import cx_Oracle
import pandas as pd

cx_Oracle.init_oracle_client(lib_dir=r"C:\Oracle\instantclient_21_3")

# # Execute the below procedure in SQL DB/ Query of the TABLE
# # STEP 1----------------------------------------------------------
# CREATE OR REPLACE PROCEDURE INS_CEO_DETAILS (P_F_NAME VARCHAR2, P_L_NAME VARCHAR2, P_COMPANY VARCHAR2, P_AGE NUMBER)
# IS
# BEGIN
# INSERT INTO CEO_DETAILS VALUES (P_F_NAME, P_L_NAME, P_COMPANY, P_AGE);
# COMMIT;
# END;

try:
    con = cx_Oracle.connect('TRAINEE19/TRAINEE19@//192.168.0.99:1521/rmclient')
except Exception as err:
    print('Error while creating the connection ', err)
else:
    try:
        cur = con.cursor()
        f_name = input('First Name : ')
        l_name = input('Last Name : ')
        Company = input('Company : ')
        age = input('Age : ')
        ID = input('New_ID : ')
        data = [f_name, l_name, Company, age, ID]
        cur.callproc('INS_CEO_DETAILS', data)
    except Exception as err:
        print('Exception occurred while fetching the record', err)
    else:
        print('Procedure INS_CEO_DETAILS executed.')
    finally:
        cur.close()
finally:
    con.close()