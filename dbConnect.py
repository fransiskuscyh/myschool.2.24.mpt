import pymysql
class mainDB:
    print("Login")

    def connect(self):
        #username = str(input("Username: "))
        #passwords = str(input("Password: "))
        # con = pymysql.connect(host='localhost', port=3306,
        con = pymysql.connect(host='db-myschool.cpsu4lo0ktjr.us-east-1.rds.amazonaws.com', port=3306,

                              user="root",
                              password="root12345",
                            #   password="",
                              database="myschool",

                              )
        cur = con.cursor()
        return con, cur

