import pyodbc
# https://datatofish.com/how-to-connect-python-to-ms-access-database-using-pyodbc/

class wpe_host():        
    def __init__(self):
       self.host_list = []  # Create an empty list
       self.conn  = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Python\access\home.mdb;')   
    
    def Get_File_Info(self):   
       build_sql = 'select * from ChallengeQuestions' 
       cur = self.conn.cursor()
       cur.execute(build_sql)  
       for row in cur.fetchall():
          self.host_list.append(row)
          
    def Show_All(self):
       for one_host in self.host_list:  
          print(one_host) 
      
    def Do_Any_SQL(self, sql_parm):
       if debug_mode:
          print("SQL: {}".format(sql_parm)) 
          # ans = input("Debug")
          return   
       if show_sql:
          print("SQL: {}".format(sql_parm))     
       cur = self.conn.cursor()
       cur.execute(sql_parm)         
       self.conn.commit()
       
    def Show_Tables(self):       
       crsr = self.conn.cursor()
       for table_info in crsr.tables(tableType='TABLE'):
          print(table_info.table_name)


    
if __name__ == "__main__":      
    wpe_instance = wpe_host()
    wpe_instance.Show_Tables()
    # wpe_instance.Get_File_Info()
    # wpe_instance.Show_All()          
    