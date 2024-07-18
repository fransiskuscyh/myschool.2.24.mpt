import tkinter as tk
import tkinter
from tkinter import messagebox,ttk
import customtkinter as ct
class Pengurus(ct.CTkFrame):
    def __init__(self, conn, cursor,master):
        super().__init__(master)
        self.curr = cursor
        self.conn = conn
    def show_pengurus(self):
        search = input("Input NUPTK Pengurus yang ingin datanya dicari?")
        self.curr.execute('SELECT * FROM pengurus WHERE NUPTK_Pengurus =' + search)
        result = self.curr.fetchall()
        print(result)
    def show_pengurusall(self):
        self.curr.execute ('SELECT * FROM pengurus')
        result = self.curr.fetchall()
        print(result)
    def tambahpengurus (self):
        Nama_Pengurus = input("Nama Pengurus yang mau dimasukkan :")
        Jabatan_Pengurus = input("Jabatan Pengurus yang mau dimasukkan :")
        NUPTK_Pengurus = input("NUPTK Pengurus yang mau dimasukkan :")
        MataPelajaran_Pengurus = input("Mata Pelajaran Pengurus yang mau dimasukkan :")
        TTL_Pengurus = input("Input TTL Pengurus yang mau dimasukkan :")
        print('Menambahkan data pengurus...')
        query = 'INSERT INTO pengurus (Nama_Pengurus, Jabatan_Pengurus, NUPTK_Pengurus, MataPelajaran_Pengurus, TTL_Pengurus) VALUES ("' + Nama_Pengurus +'","'+ Jabatan_Pengurus + '","'+ NUPTK_Pengurus + '","' + MataPelajaran_Pengurus + '","' + TTL_Pengurus + '")'
        self.curr.execute(query)
        self.conn.commit()
        print('Proses penambahan selesai')

    def __deletedatapengurus(self):
        pilih = input("Silahkan pilih mau menghapus data yang mana? (Input NUPTK)").title()
        print("Menghapus data pengurus....")
        query = 'DELETE FROM `pengurus` WHERE NUPTK_Pengurus = "' + pilih + '"';
        self.curr.execute(query)
        self.conn.commit()
        print("Data Pengurus dengan NUPTK", pilih, "berhasil dihapus....")
    def valueProfilePengurus(self,column,username,xframe,yframe,xlabel,ylabel,label,masterss):
        sql1 = 'select `pengurus`.{} from `pengurus` inner join `pengurus_account` on `pengurus`.NUPTK_Pengurus=`pengurus_account`.nuptk where `pengurus_account`.user_pengurus = (%s);'.format(
            column)
        self.curr.execute(sql1, (username))
        result = self.curr.fetchone()
        for x in result:
            self.hasil = x

        self.frameBio(self.hasil, xframe, yframe,masterss)
        self.labelBio(label, xlabel, ylabel,masterss)

    def frameBio(self,text,xframe,yframe,masterss):
        self.bioFrame = ct.CTkFrame(master=masterss, width=385, height=40,fg_color='#f2f2f2', corner_radius=15 )
        self.bioFrame.place(relx=xframe, rely=yframe, anchor=tkinter.NW)
        self.bioLabel = ct.CTkLabel(master=self.bioFrame, text_color='black', text=text)
        self.bioLabel.place(relx=0.05,rely=0.5, anchor=tkinter.W)

    def labelBio(self,text,relx,rely,masterss):
        font2 = ct.CTkFont(family='montserrat', size=18)
        self.LabelatasBio = ct.CTkLabel(master=masterss, text=text,font=font2, text_color='black')
        self.LabelatasBio.place(relx=relx,rely=rely,anchor=tkinter.NW)



