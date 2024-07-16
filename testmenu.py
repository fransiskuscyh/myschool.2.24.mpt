from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
import random
import pymysql
from datetime import datetime
import numpy as np 
from PIL import Image, ImageTk

root=tkinter.Tk()
root.title("Halaman Kelas")
root.geometry("800x640")
myClass = ttk.Treeview(root,show='headings',height=20)
style = ttk.Style()
placeholderArray = ['','','','','','']

# menu 
min_w = 65 
max_w = 150
cur_width = min_w
expanded = False

def connection():
    conn=pymysql.connect(
        host='localhost',
        user='root',
        password='', 
        db='ruangkelas'
    )
    return conn

conn=connection()
cursor=conn.cursor()

for i in range(0,5):
    placeholderArray[i]=tkinter,StringVar()

dummyData=[
    ['bunga bangsa',11,'siti','asep',10],
    ['bunga mawar',7,'wulan','petir',50],
    ['harapan bangsa',12,'lestari','hana',60]
]

def read():
    cursor.connection.ping()
    sql=f"SELECT * FROM kelas ORDER BY 'nama_kelas' DESC"
    cursor.execute(sql)
    results=cursor.fetchall()
    conn.commit()
    conn.close()
    return results


def refreshTable():
    for data in myClass.get_children():
        myClass.delete(data)
    for array in read():
        myClass.insert(parent='',index='end',iid=array,text="",values=(array),tags="orow")
    myClass.tag_configure("orow",background="#FFF")

def hasil():
    show(root)

def kelas():
    import kelasv3Gui
    kelasv3Gui()
    kelas()

def formTampilan(self):
    myClass['columns']=("nama_kelas", "tingkat_kelas", "wali_kelas", "ketua_kelas", "jumlah")

    myClass.column("#0",width=0,stretch=NO)
    myClass.column("nama_kelas",anchor=W,width=155)
    myClass.column("tingkat_kelas",anchor=W,width=155)
    myClass.column("wali_kelas",anchor=W,width=155)
    myClass.column("ketua_kelas",anchor=W,width=155)
    myClass.column("jumlah",anchor=W,width=155)

    myClass.heading("nama_kelas",text="nama_kelas",anchor=W)
    myClass.heading("tingkat_kelas",text="tingkat_kelas",anchor=W)
    myClass.heading("wali_kelas",text="wali_kelas",anchor=W)
    myClass.heading("ketua_kelas",text="ketua_kelas",anchor=W)
    myClass.heading("jumlah",text="jumlah",anchor=W)

    myClass.tag_configure("now",background="#fff")
    myClass.pack()
    refreshTable()

def expand():
    global cur_width, expanded
    cur_width += 8
    rep = root.after(10,expand)
    frame.config(width=cur_width)
    if cur_width >= max_w: 
        expanded = True 
        root.after_cancel(rep) 
        fill()

def contract():
    global cur_width, expanded
    cur_width -= 10 
    rep = root.after(5,contract) 
    frame.config(width=cur_width) 
    if cur_width <= min_w: 
        expanded = False 
        root.after_cancel(rep) 
        fill()

def fill():
    if expanded: 
        home_b.config(image=home1)
        set_b.config(image=home1)
        ring_b.config(image=home1)
    else:
        home_b.config(image=home,font=(0,21))
        set_b.config(image=settings,font=(0,21))
        ring_b.config(image=ring,font=(0,21))

home1 = ImageTk.PhotoImage(Image.open('home1.png').resize((120,40)))
home = ImageTk.PhotoImage(Image.open('home.png').resize((40,40)))
settings = ImageTk.PhotoImage(Image.open('add.png').resize((40,40)))
ring = ImageTk.PhotoImage(Image.open('add.png').resize((40,40)))

root.update()
frame = Frame(root,bg='blue',width=65,height=root.winfo_height())
frame.grid(row=0,column=0) 

home_b = Button(frame,image=home,bg='blue',relief='flat', command=hasil)
set_b = Button(frame,image=settings,bg='blue',relief='flat')
ring_b = Button(frame,image=ring,bg='blue',relief='flat')

home_b.grid(row=0,column=0,pady=15,padx=5)
set_b.grid(row=1,column=0,pady=50)
ring_b.grid(row=2,column=0)

frame.bind('<Enter>',lambda e: expand())
frame.bind('<Leave>',lambda e: contract())

def show(self):
    style.configure(root)
    myClass.columnconfigure(1,weight=1)
    myClass.columnconfigure(2,weight=1)
    myClass.columnconfigure(3,weight=1)
    myClass.columnconfigure(4,weight=1)
    myClass.columnconfigure(5,weight=1)
    myClass.columnconfigure(6,weight=1)

    myClass['columns']=("nama_kelas", "tingkat_kelas", "wali_kelas", "ketua_kelas", "jumlah")

    myClass.column("#0",width=0,stretch=NO)
    myClass.column("nama_kelas",anchor=W,width=155)
    myClass.column("tingkat_kelas",anchor=W,width=155)
    myClass.column("wali_kelas",anchor=W,width=155)
    myClass.column("ketua_kelas",anchor=W,width=155)
    myClass.column("jumlah",anchor=W,width=155)

    myClass.heading("nama_kelas",text="nama_kelas",anchor=W)
    myClass.heading("tingkat_kelas",text="tingkat_kelas",anchor=W)
    myClass.heading("wali_kelas",text="wali_kelas",anchor=W)
    myClass.heading("ketua_kelas",text="ketua_kelas",anchor=W)
    myClass.heading("jumlah",text="jumlah",anchor=W)
    myClass.pack()

    myClass.tag_configure("now",background="#fff")
    refreshTable()

frame.grid_propagate(False)

root.mainloop()
