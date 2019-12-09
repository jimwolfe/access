import pyodbc
# https://datatofish.com/how-to-connect-python-to-ms-access-database-using-pyodbc/


    
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\html\home.mdb;')
cursor = conn.cursor()
cursor.execute('select * from Passwords')
   
for row in cursor.fetchall():
    print (row)