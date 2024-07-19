#import login
import tkinter
from dbConnect import *
from testSiswa import *
from mataPel import *
from pengurus import *


#root = tk.Tk()
dbApp = mainDB()
conn_dbApp, curr_dbApp = dbApp.connect()

x_siswa = Siswa(conn=conn_dbApp, curr=curr_dbApp)
#x_mapel = matapelajaran(conn=conn_dbApp, curr=curr_dbApp)
tbl_pengurus = Pengurus(conn=conn_dbApp, cursor=curr_dbApp)
x_kelas = kelas(conn=conn_dbApp, curr=curr_dbApp)
#x_absensi = absensi(conn=conn_dbApp, curr=curr_dbApp)
#x_nilai = nilai(con=conn_dbApp, cur=curr_dbApp)
#login_page = LoginPage(root)



def appOperation():
    while True:
        pilihan = str(input("""Silahkan Pilih:
        1. Siswa
        2. Mata Pelajaran
        3. Pengurus
        4. Kelas
        5. Absensi
        6. Nilai
        7. Log Out
Masukkan Pilihan: """))
        if pilihan == "1":
            x_siswa.siswaOperation()
        elif pilihan == "2":
            x_mapel.mapelOperation()
        elif pilihan == "3":
            tbl_pengurus.pengurusOperation()
        elif pilihan == "4":
            x_kelas.kelasOperation()
        elif pilihan == "5":
            x_absensi.absensiOperation()
        elif pilihan == "6":
            x_nilai.home()
        elif pilihan == "7":
            print("Logged Out!!!")
            break
        else:
            print("Masukkan Pilihan yang Benar!!!")
            continue
#sql111 = 'CREATE TABLE data_siswa( nama VARCHAR(255) NOT NULL DEFAULT "", kelas VARCHAR(255) NOT NULL DEFAULT "", nis INT NOT NULL DEFAULT 0, gender ENUM("Pria","Wanita","") NOT NULL DEFAULT "");'
#curr_dbApp.execute(sql111)
#sql112 = 'FLUSH PRIVILEGES;'
#curr_dbApp.execute(sql112)
#conn_dbApp.commit()

#root.mainloop()








