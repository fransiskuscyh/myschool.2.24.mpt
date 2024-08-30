import tkinter as tk
from tkinter import Scrollbar, RIGHT, Y
import tkinter
from tkinter import messagebox, ttk
import customtkinter as ct
import pymysql
import statistics as st

class mataPelajaranSiswa(ct.CTkFrame):
    def __init__(self, curr, conn,master):
        super().__init__(master)
        self.curr = curr
        self.conn = conn
        self.font_mataPelajaran = ct.CTkFont(family='montserrat', size=17)
        # self.xonn = pymysql.connect(host='localhost', port=3306, user="root", password="", database="myschool",)
        self.xonn = pymysql.connect(host='db-myschool.cpsu4lo0ktjr.us-east-1.rds.amazonaws.com', port=3306, user="root", password="root12345", database="myschool",)
        self.showMapel = self.xonn.cursor()
        self.showMapel.execute("select * from mata_pelajaran")

    def setup_uimatapelajaranSiswa(self, masterss):

        self.table = ttk.Treeview(masterss, columns=("id", "mataPelajaran", "pengajar"), show="headings")
        self.table.heading("id", text="id")
        self.table.heading("mataPelajaran", text="mataPelajaran")
        self.table.heading("pengajar", text="pengajar")
        self.table.column("id", width=150)
        self.table.column("mataPelajaran", width=300)
        self.table.column("pengajar", width=300)
        self.refreshTable()
        

        scroll = ttk.Scrollbar(masterss, orient='vertical', command=self.table.yview)
        self.table.configure(yscrollcommand=scroll.set)

        self.table.grid(row=0, column=0, sticky="nsew")
        scroll.grid(row=0, column=1, sticky="ns")


    def on_tree_select(self, event):
        selected_item = self.table.selection()
        if selected_item:
            item = self.table.item(selected_item)
            values = item["values"]
            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0, values[0])
            self.entry_mataPelajaran.delete(0, tk.END) 
            self.entry_mataPelajaran.insert(0, values[1])
            self.entry_pengajar.delete(0, tk.END) 
            self.entry_pengajar.insert(0, values[2])
            
    def refreshTable(self,):
        for data in self.table.get_children():
            self.table.delete(data)
        for x in self.showMapel:
            self.table.insert('', tkinter.END, values=x[0:])
