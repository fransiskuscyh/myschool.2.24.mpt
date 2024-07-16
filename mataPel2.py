import tkinter as tk
from tkinter import messagebox,ttk
import customtkinter as ct
from main import *
import statistics as st
# dbApp = mainDB()
# conn_dbApp, curr_dbApp = dbApp.connect()

class mataPelajaran (ct.CTk):
    def __init__(self,curr,conn):
        super().__init__()


        self.curr = curr
        self.conn = conn
        self.font_mataPelajaran = ct.CTkFont(family='montserrat', size=17)


    def setup_uimatapelajaran(self,masterss):

        self.id = ct.CTkLabel(master=masterss, text="ID",anchor="e",justify = "right",width=60,font=self.font_mataPelajaran)
        self.mataPelajaran = ct.CTkLabel(master=masterss, text="MataPelajaran",anchor="e",justify = "right",width=60,font=self.font_mataPelajaran)
        self.pengajar = ct.CTkLabel(master=masterss, text="Pengajar",anchor="e",justify = "right",width=60,font=self.font_mataPelajaran)
        
        self.id.place(x=50, y=40)
        self.mataPelajaran.place(x=50, y=70)
        self.pengajar.place(x=50, y=100)

        self.id_var = tk.StringVar()
        self.mataPelajaran_var = tk.StringVar()
        self.pengajar_var = tk.StringVar()

        self.entry_id = ct.CTkEntry(master=masterss, font=self.font_mataPelajaran, textvariable=self.id_var, width = 400)
        self.entry_id.place(x=200, y=40)
        self.entry_mataPelajaran = ct.CTkEntry(master=masterss, font=self.font_mataPelajaran, textvariable=self.mataPelajaran_var, width = 400)
        self.entry_mataPelajaran.place(x=200, y=70)
        self.entry_pengajar = ct.CTkEntry(master=masterss, font=self.font_mataPelajaran, textvariable=self.pengajar_var, width = 400)
        self.entry_pengajar.place(x=200, y=100)

        self.columns = ('id', 'mataPelajaran', 'pengajar')
        self.table = ttk.Treeview(master=masterss, columns=self.columns, show='headings', height=1000)
        self.table.heading('id', text='ID')
        self.table.column('id', minwidth=0, width=185, stretch=False)
        self.table.heading('mataPelajaran', text='MataPelajaran')
        self.table.column('mataPelajaran', minwidth=0, width=185, stretch=False)
        self.table.heading('pengajar', text='Pengajar')
        self.table.column('pengajar', minwidth=0, width=185, stretch=False)

        self.table.place(x=50,y=250)

        self.button_save = ct.CTkButton(master= masterss, height=42, width=144, text='Save', fg_color="orange", hover_color="blue", font=('montserrat',17), command=self.save)
        self.button_edit = ct.CTkButton(master= masterss, height=42, width=144, text='Edit', fg_color="orange", hover_color="blue", font=('montserrat',17), command=self.ubah_data)
        self.button_delete = ct.CTkButton(master= masterss, height=42, width=144, text='Delete', fg_color="orange", hover_color="blue", font=('montserrat',17), command=self.delete_data)
        self.button_save.place(x=655, y=40)
        self.button_edit.place(x=655, y=90)
        self.button_delete.place(x=655, y=140)

    def read(self):
        self.curr.connection.ping()
        sql=f"SELECT * FROM mata_pelajaran" 
        self.curr.execute(sql)
        results=self.curr.fetchall()
        self.conn.commit()
        self.conn.close()
        return results


    def refreshTable():
        for data in mataPelajaran.get_children():
            mataPelajaran.delete(data)
        for array in mataPelajaran.read():
            mataPelajaran.insert(parent='',index='end',iid=array,text="",values=(array),tags="orow")
        mataPelajaran.tag_configure("orow",background="#FFF")
        mataPelajaran.pack()
        
    def save(self):
        id = str(self.entry_id.get())
        matapelajaran = str(self.entry_mataPelajaran.get())
        pengajar = str(self.entry_pengajar.get())
        if not(id and id.strip()) or not(matapelajaran and matapelajaran.strip()) or not(pengajar and pengajar.strip()) :
            messagebox.showwarning("","PLEASE FILL UP ALL ENTRIES!")
            return
        try:
            self.curr.connection.ping()
            sql=f"SELECT * FROM mata_pelajaran WHERE 'id'='{id}' "
            self.curr.execute(sql, )
            checkid=self.curr.fetchall()
            if len(checkid) > 0:
                messagebox.showwarning("","already use!")
                return
            if len(id) < 3:
                messagebox.showwarning("", "Invalid Item ID")
            else:
                self.curr.connection.ping()
                sql = f"INSERT INTO mata_pelajaran (`id`, `mataPelajaran`, `pengajar`) VALUES ('{id}','{matapelajaran}','{pengajar}')"
                self.curr.execute(sql, )
            self.conn.commit()
            self.conn.close()             
        except: 
            messagebox.showwarning("","error while save")
            return

    def ubah_data(self):
        id = str(self.entry_id.get())
        matapelajaran = str(self.entry_mataPelajaran.get())
        pengajar = str(self.entry_pengajar.get())
        if not(id and id.strip()) or not(matapelajaran and matapelajaran.strip()) or not(pengajar and pengajar.strip()) :
            messagebox.showwarning("","PLEASE FILL UP ALL ENTRIES!")
            return
        try:
            self.curr.connection.ping()
            sql=f"SELECT * FROM mata_pelajaran 'id'='{id}' "
            self.curr.execute(sql, )
            checkNamaKelas=self.curr.fetchall()
            if len(checkNamaKelas) > 0:
                messagebox.showwarning("","already use!")
                return
            if len(id) < 5:
                messagebox.showwarning("", "Invalid Item ID")
            else:
                self.curr.connection.ping()
                sql = f"UPDATE mata_pelajaran SET 'mataPelajaran' = '{matapelajaran}', 'pengajar' = '{pengajar}'')"
                self.curr.execute(sql, )
            self.conn.commit()
            self.conn.close()             
        except: 
            messagebox.showwarning("","error while save")
            return

    def delete_data(self):
        id = str(self.entry_id.get())
        matapelajaran = str(self.entry_mataPelajaran.get())
        pengajar = str(self.entry_pengajar.get())
        if not(id and id.strip()) or not(matapelajaran and matapelajaran.strip()) or not(pengajar and pengajar.strip()) :
            messagebox.showwarning("","PLEASE FILL UP ALL ENTRIES!")
            return
        try:
            self.curr.connection.ping()
            sql=f"SELECT * FROM mata_pelajaran WHERE 'id'='{id}' "
            self.curr.execute(sql, )
            checkNamaKelas=self.curr.fetchall()
            if len(checkNamaKelas) > 0:
                messagebox.showwarning("","already use!")
                return
            if len(id) < 3:
                messagebox.showwarning("", "Invalid Item ID")
            else:
                self.curr.connection.ping()
                sql = f"DELETE FROM `mata_pelajaran` WHERE `id` = '{id}'"
                self.curr.execute(sql, )
            self.conn.commit()
            self.conn.close()             
        except: 
            messagebox.showwarning("","error while save")
            return