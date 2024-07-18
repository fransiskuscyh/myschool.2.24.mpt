import pymysql
class mainDB:
    print("Login")

    def connect(self):
        #username = str(input("Username: "))
        #passwords = str(input("Password: "))
        con = pymysql.connect(host='localhost', port=3306,

                              user="root",
                              password="",
                              database="myschool",

                              )
        cur = con.cursor()
        return con, cur

