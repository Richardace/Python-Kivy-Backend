import mysql.connector

class Conexion:
    
    user="root"
    passw=""
    hos="localhost"
    db="musica"
    mydb=None
    
    def __init__(self):
        self.mydb = mysql.connector.connect(host=self.hos, user=self.user, passwd=self.passw , database=self.db)

    def select(self,instrucc):
        ins=self.mydb.cursor()
        ins.execute(instrucc)
        return ins.fetchall()

    def insert(self,sql,val):
        ins=self.mydb.cursor()
        ins.execute(sql,val)
        self.mydb.commit()
        print(ins.rowcount, "was inserted.")
        return True