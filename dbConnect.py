import pymysql
class mainDB:
    print("Login")

    def connect(self):
        #username = str(input("Username: "))
        #passwords = str(input("Password: "))
        con = pymysql.connect(host='database-myschool.ciqnmiwbcceb.us-east-1.rds.amazonaws.com', port=3306,

                              user="root",
                              password="vando1234",
                              database="siswa",

                              )
        cur = con.cursor()
        return con, cur

