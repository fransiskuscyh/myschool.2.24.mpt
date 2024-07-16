from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
import random 
import pymysql
from datetime import datetime
import numpy as np 

root=tkinter.Tk()
root.title("Halaman Kelas")
root.geometry("800x640")
myClass = ttk.Treeview(root,show='headings',height=20)
style = ttk.Style()
placeholderArray = ['','','','','','']
numeric = '1234567890'
alpha = 'ABCDEFGHIJKLMNOPQRSTUWXYZ'

def connection():
    conn=pymysql.connect(
        host='database-myschool.ciqnmiwbcceb.us-east-1.rds.amazonaws.com', port=3306,
        user='root',
        password='vando1234',
        db='siswa'
    )
    return conn

conn=connection()
cursor=conn.cursor()

for i in range(0,5):
    placeholderArray[i]=tkinter,StringVar()

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
    # for array in read():
    #     myClass.insert(parent='',index='end',iid=array,text="",values=(array),tags="orow")
    # myClass.tag_configure("orow",background="#FFF")
    myClass.pack()

def setph(self,word,num):
    for ph in range(0,5):
        if ph == num:
            placeholderArray[ph].set(word)

def generateRand(self):
    namaKelas=''
    for i in range(0,3):
        randno=random.randrange(0,(len(numeric)-1))
        namaKelas=namaKelas+str(numeric[randno])
    randno=random.randrange(0,(len(alpha)-1))
    print("generated:"-namaKelas)
    setph(namaKelas,0)    

def save():
    nama=str(namaKelas.get())
    tingkat=str(tingkatKelas.get())
    wali=str(waliKelas.get())
    ketua=str(ketuaKelas.get())
    jum=str(jumlah.get())
    if not(nama and nama.strip()) or not(tingkat and tingkat.strip()) or not(wali and wali.strip()) or not(ketua and ketua.strip()) or not(jum and jum.strip()):
        messagebox.showwarning("","PLEASE FILL UP ALL ENTRIES!")
        return
    try:
        cursor.connection.ping()
        sql=f"SELECT * FROM kelas WHERE 'nama_kelas'='{nama}' "
        cursor.execute(sql)
        checkNamaKelas=cursor.fetchall()
        if len(checkNamaKelas) > 0:
            messagebox.showwarning("","already use!")
            return
        if len(nama) < 5:
            messagebox.showwarning("", "Invalid Item Name")
        else:
            cursor.connection.ping()
            sql = f"INSERT INTO kelas (`nama_kelas`, `tingkat_kelas`, `wali_kelas`, `ketua_kelas`, `jumlah`) VALUES ('{nama}','{tingkat}','{wali}','{ketua}','{jum}')"
            cursor.execute(sql)
        conn.commit()
        conn.close()             
    except: 
        messagebox.showwarning("","error while save")
        return
    refreshTable()

def update():
    selectedNama = ''
    try:
        selectedNama = myClass.selection()[0]
        selectedNama = str(myClass.item(selectedNama)['values'][0])
    except:
        messagebox.showwarning("", "PLEASE SELECT A DATE ROW")
    print(selectedNama)
    nama=str(namaKelas.get())
    tingkat=str(tingkatKelas.get())
    wali=str(waliKelas.get())
    ketua=str(ketuaKelas.get())
    jum=str(jumlah.get())
    if not(nama and nama.strip()) or not(tingkat and tingkat.strip()) or not(wali and wali.strip()) or not(ketua and ketua.strip()) or not(jum and jum.strip()):
        messagebox.showwarning("", "PLEASE FILL UP ALL ENTRIES")
        return
    if (selectedNama!=nama):
        messagebox.showwarning(""< "YOU CAN'T CHANGE NAMA")
        return
    try:
        cursor.connection.ping()
        sql=f"UPDATE kelas SET 'tingkat_kelas' = '{tingkat}', 'wali_kelas' = '{wali}', 'ketua_kelas' = '{ketua}', 'jumlah' = '{jum}' WHERE 'nama_kelas' = '{nama}'"
        # sql = f"UPDATE kelas SET (`nama_kelas`, `tingkat_kelas`, `wali_kelas`, `ketua_kelas`, `jumlah`) VALUES ('{nama}','{tingkat}','{wali}','{ketua}','{jum}')"
        cursor.execute(sql)
        conn.commit()
        conn.close()             
    except Exception as err: 
        messagebox.showwarning("","ERROR occured ref: "+str(err))
        return
    refreshTable()

def select():
    selectedNama = ''
    try:
        selectedNama = myClass.selection()[0]
        nama = str(myClass.item(selectedNama)['values'][0])
        tingkat = str(myClass.item(selectedNama)['values'][1])
        wali = str(myClass.item(selectedNama)['values'][2])
        ketua = str(myClass.item(selectedNama)['values'][3])
        jum = str(myClass.item(selectedNama)['values'][4])
        setph(nama,0)
        setph(tingkat,1)
        setph(wali,2)
        setph(ketua,3)
        setph(jum,4)
    except:
        messagebox.showwarning("", "PLEASE SELECT A DATA ROW")

def close():
    exit()

frameMode=tkinter.Frame(root,bg="#02577A")
frameMode.pack()

buttonColor="#196E78"

manageFrame=tkinter.LabelFrame(frameMode,text="Manage",borderwidth=5)
manageFrame.grid(row=0,column=0,sticky="w",padx=[10,200],ipadx=[6])

entryFrame=tkinter.LabelFrame(frameMode,text="Form",borderwidth=5)
entryFrame.grid(row=1,column=0,sticky="w",padx=[10,200],pady=[10,30],ipadx=[6])

# inputan
namaKelas=Label(entryFrame,text="nama_kelas",anchor="e",width=10)
tingkatKelas=Label(entryFrame,text="tingkat_kelas",anchor="e",width=10)
waliKelas=Label(entryFrame,text="wali_kelas",anchor="e",width=10)
ketuaKelas=Label(entryFrame,text="ketua_kelas",anchor="e",width=10)
jumlah=Label(entryFrame,text="jumlah",anchor="e",width=10)

namaKelas.grid(row=0,column=0,padx=5)
tingkatKelas.grid(row=1,column=0,padx=5)
waliKelas.grid(row=2,column=0,padx=5)
ketuaKelas.grid(row=3,column=0,padx=5)
jumlah.grid(row=4,column=0,padx=5)

namaKelas=Entry(entryFrame,width=50,textvariable=placeholderArray[0])
tingkatKelas=Entry(entryFrame,width=50,textvariable=placeholderArray[1])
waliKelas=Entry(entryFrame,width=50,textvariable=placeholderArray[2])
ketuaKelas=Entry(entryFrame,width=50,textvariable=placeholderArray[3])
jumlah=Entry(entryFrame,width=50,textvariable=placeholderArray[4])

namaKelas.grid(row=0,column=2,padx=5,pady=5)
tingkatKelas.grid(row=1,column=2,padx=5,pady=5)
waliKelas.grid(row=2,column=2,padx=5,pady=5)
ketuaKelas.grid(row=3,column=2,padx=5,pady=5)
jumlah.grid(row=4,column=2,padx=5,pady=10)

saveBtn=Button(entryFrame,text="SAVE", borderwidth=3, command=save)
saveBtn.grid(row=5,column=2,padx=5,pady=5)

cancelBtn=Button(entryFrame,text="cancel", borderwidth=3, command=close)
cancelBtn.grid(row=5,column=1,padx=5,pady=5)

style.configure(root)

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



# refreshTable()
# root.resizable(False,False)
# root.mainloop()