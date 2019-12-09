import pyodbc
# https://stackoverflow.com/questions/39995802/create-new-access-database-and-tables-using-python
dbname = r'C:\Python\access\work.mdb'
table_sql = ('CREATE TABLE Table2 (' 
  ' ID autoincrement,'
  ' Col1 varchar(50),'
  ' Col2 double,'
  ' Col3 datetime);')
                
class wpe_host():        
    def __init__(self):                   
       constr = "DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={0};".format(dbname)
       self.conn = pyodbc.connect(constr)
       cur = self.conn.cursor()
       try:
          cur.execute('DROP TABLE Table2;')
       except:
          print("No table to drop")                    
       cur.execute(table_sql)                 
       self.conn.commit()

if __name__ == "__main__":  
    wpe_instance = wpe_host()
    
    