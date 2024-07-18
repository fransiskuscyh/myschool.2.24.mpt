import tkinter as tk
import tkinter
from tkinter import messagebox,ttk
import customtkinter as ct
class Siswa(ct.CTkFrame):
    def __init__(self,curr,conn,master):
        super().__init__(master)
        self.conn = conn
        self.curr = curr
    def tambahDataSiswa(self,namaSiswa, kelasSiswa, nisSiswa, genderSiswa):
        sql = "INSERT INTO `data_siswa` (`nama`, `kelas`, `nis`, `gender`) VALUES (%s, %s, %s, %s)"
        self.curr.execute(sql, (namaSiswa, kelasSiswa, nisSiswa, genderSiswa))
        self.conn.commit()
        sql2 = "SELECT * FROM `data_siswa` WHERE `nis` = (%s)"
        self.curr.execute(sql2,(nisSiswa))
        hasil = self.curr.fetchall()
        print(hasil)

    def __deleteDataSiswa(self,nisSiswa):
        sql = "DELETE FROM `data_siswa` WHERE `nis` = %s"
        self.curr.execute(sql, (nisSiswa))
        print("Data Telah Dihapus!")
        self.conn.commit()

    def showDataSiswa(self, nisSiswa):
        sql2 = "SELECT * FROM `data_siswa` WHERE `nis` = (%s)"
        self.curr.execute(sql2, (nisSiswa))
        result = self.curr.fetchall()
        print(result)

    def showDataSiswaAll(self):
        sql2 = "SELECT * FROM `data_siswa`"
        self.curr.execute(sql2)
        result = self.curr.fetchall()
        for row in result:
            print(row)


    def setNamaSiswa(self,namaSiswa,nisSiswa):
        sql = "UPDATE `data_siswa` SET `nama` = (%s) WHERE `nis` = (%s)"
        self.curr.execute(sql, (namaSiswa, nisSiswa))
        sql2 = "SELECT * FROM `data_siswa` WHERE `nis` = (%s)"
        self.curr.execute(sql2, (nisSiswa))
        result = self.curr.fetchone()
        print(result)
        self.conn.commit()

    def setKelasSiswa(self,kelasSiswa,nisSiswa):
        kolom = input("")
        sql = "UPDATE `data_siswa` SET (%s) = (%s) WHERE `nis` = (%s)"
        self.curr.execute(sql, (kolom,kelasSiswa, nisSiswa))
        sql2 = "SELECT * FROM `data_siswa` WHERE `nis` = (%s)"
        self.curr.execute(sql2, (nisSiswa))
        result = self.curr.fetchone()
        print(result)
        self.conn.commit()

    def setNISSiswa(self, nisLama, nisBaru):
        sql = "UPDATE `data_siswa` SET `nis` = (%s) WHERE `nis` = (%s)"
        self.curr.execute(sql, (nisBaru, nisLama))
        sql2 = "SELECT * FROM `data_siswa` WHERE `nis` = (%s)"
        self.curr.execute(sql2, (nisBaru))
        result = self.curr.fetchone()
        print(result)
        self.conn.commit()

    def setGenderSiswa(self,genderSiswa,nisSiswa):
        sql = "UPDATE `data_siswa` SET `gender` = (%s) WHERE `nis` = (%s)"
        self.curr.execute(sql, (genderSiswa, nisSiswa))
        sql2 = "SELECT * FROM `data_siswa` WHERE `nis` = (%s)"
        self.curr.execute(sql2, (nisSiswa))
        result = self.curr.fetchone()
        print(result)
        self.conn.commit()

    def valueProfile(self,column,username,xframe,yframe,xlabel,ylabel,masterss):
        sql1 = 'select `data_siswa`.{} from `data_siswa` inner join `user_account` on `data_siswa`.nis=`user_account`.nis where `user_account`.username = (%s);'.format(
            column)
        self.curr.execute(sql1, (username))
        result = self.curr.fetchone()
        for x in result:
            self.hasil = x

        self.frameBio(self.hasil,xframe,yframe,masterss)
        self.labelBio(column.upper(),xlabel,ylabel,masterss)

    def frameBio(self,text,xframe,yframe,masterss):
        self.bioFrame = ct.CTkFrame(master=masterss, width=385, height=40,fg_color='#f2f2f2', corner_radius=15 )
        self.bioFrame.place(relx=xframe, rely=yframe, anchor=tkinter.NW)
        self.bioLabel = ct.CTkLabel(master=self.bioFrame, text_color='black', text=text)
        self.bioLabel.place(relx=0.05,rely=0.5, anchor=tkinter.W)

    def labelBio(self,text,relx,rely,masterss):
        font2 = ct.CTkFont(family='montserrat', size=18)
        self.LabelatasBio = ct.CTkLabel(master=masterss, text=text,font=font2, text_color='black')
        self.LabelatasBio.place(relx=relx,rely=rely,anchor=tkinter.NW)


