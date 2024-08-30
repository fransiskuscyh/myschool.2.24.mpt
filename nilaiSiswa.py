import tkinter as tk
from tkinter import messagebox,ttk
import tkinter
import customtkinter as ct
import pymysql
import statistics as st

class nilaiSiswa(ct.CTkFrame):
    def __init__(self,curr,conn,master):
        super().__init__(master)

        # self.conn = pymysql.connect(host='localhost', port=3306, user="root", password="", database="myschool",)
        self.conn = pymysql.connect(host='db-myschool.cpsu4lo0ktjr.us-east-1.rds.amazonaws.com', port=3306, user="root", password="root12345", database="myschool",)
        self.showNilai = self.conn.cursor()
        self.showNilai.execute("select * from nilai")
        self.curr = curr
        self.conn = conn
        self.font = ct.CTkFont(family='montserrat', size=17)


    def nilaiSiswaUi(self,masterss):

        self.columns = ('id', 'nama', 'kelas', 'matkul', 'nilai tugas', 'nilai ujian', 'rata-rata')
        self.table = ttk.Treeview(master=masterss, columns=self.columns, show='headings', height=300)
        self.table.heading('id', text='ID')
        self.table.column('id', minwidth=0, width=60, stretch=False)
        self.table.heading('nama', text='Nama')
        self.table.column('nama', minwidth=0, width=140, stretch=False)
        self.table.heading('kelas', text='Kelas')
        self.table.column('kelas', minwidth=0, width=80, stretch=False)
        self.table.heading('matkul', text='Matkul')
        self.table.column('matkul', minwidth=0, width=140, stretch=False)
        self.table.heading('nilai tugas', text='Nilai Tugas')
        self.table.column('nilai tugas', minwidth=0, width=100, stretch=False)
        self.table.heading('nilai ujian', text='Nilai Ujian')
        self.table.column('nilai ujian', minwidth=0, width=100, stretch=False)
        self.table.heading('rata-rata', text='Rata-Rata')
        self.table.column('rata-rata', minwidth=0, width=100, stretch=False)
        self.refreshTable()

        # self.table.place(x=80, y=280)
        self.table.place(relx=0.05, rely=0.1)

        self.button_cari = ct.CTkButton(master=masterss, height=40, width=150, text='cari', fg_color="#00df00",
                                        font=('montserrat', 17), command=lambda: self.pemastian_murid_nilai_cari())
        self.button_cari.place(x=640, y=35)

    def refreshTable(self,):
        for data in self.table.get_children():
            self.table.delete(data)
        for x in self.showNilai:
            self.table.insert('', tkinter.END, values=x[0:])