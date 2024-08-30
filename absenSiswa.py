import tkinter as tk
from tkinter import messagebox, ttk
import customtkinter as ct
import pymysql
import statistics as st


class absenSiswa(ct.CTkFrame):
    def __init__(self, curr, conn,master):
        super().__init__(master)
        # self.conn = pymysql.connect(host='localhost', port=3306, user="root", password="", database="myschool",)
        self.conn = pymysql.connect(host='db-myschool.cpsu4lo0ktjr.us-east-1.rds.amazonaws.com', port=3306, user="root", password="root12345", database="myschool",)
        self.showAbsensi = self.conn.cursor()
        self.showAbsensi.execute("select * from absensi")
        self.curr = curr
        self.conn = conn

    def uiAbsenSiswa(self, masterss):

        self.columns = ('NIS', 'nama', 'kelas', 'mapel', 'status')
        self.table = ttk.Treeview(master=masterss, columns=self.columns, show='headings', height=300)
        self.table.heading('NIS', text='Nomor Induk Siswa')
        self.table.column('NIS', minwidth=0, width=120, stretch=False)
        self.table.heading('nama', text='Nama Siswa')
        self.table.column('nama', minwidth=0, width=120, stretch=False)
        self.table.heading('kelas', text='Kelas')
        self.table.column('kelas', minwidth=0, width=120, stretch=False)
        self.table.heading('mapel', text='Mata Pelajaran')
        self.table.column('mapel', minwidth=0, width=120, stretch=False)
        self.table.heading('status', text='Status Kehadiran')
        self.table.column('status', minwidth=0, width=120, stretch=False)
        self.refreshTable()
        self.table.pack()
        
        self.table.place(relx=0.02, rely=0.05)

        self.button_cari = ct.CTkButton(master=masterss, height=50, width=144, text='Cari', fg_color='#0060ff',
                                        font=('montserrat', 17), command=lambda: self.execute_cari())
        self.button_cari.place(x=655, y=20)


    def refreshTable(self):
        i = 0
        for ro in self.showAbsensi:
            self.table.insert("", i,text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4],))
            i = i + 1

