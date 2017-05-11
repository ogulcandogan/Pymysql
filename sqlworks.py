# -*- coding: utf-8 -*-
from tkinter import *
import pymysql

adress = 'localhost'
portnumber = 3306
username = 'root'
password = 'Şifrenizi yazınız'
dbase=input("Veritabanı adını giriniz : ")
if len(dbase)==0:
    dbase=str(input("Oluşturmak istediğiniz veri tabanı adı giriniz :"))
    conn = pymysql.connect(host=adress, port=portnumber, user=username, passwd=password)
    cur = conn.cursor()
    cur.execute("CREATE DATABASE " + dbase + " ")
try:
    conn = pymysql.connect(host=adress, port=portnumber, user=username, passwd=password, db=dbase)
except:
    exit()

pencere = Tk()
pencere.geometry("700x400")
pencere.title("Mysql Sorgu Arayüzü")


def Sorgula():
    global database
    database=''
    cur = conn.cursor()
    komut = area.get(0.0, END)
    cur.execute(" " + komut + " ")
    etiket2["text"] = "Sorgu başarıyla çalıştırılmıştır :) "
    for row in cur:
        etiket3["text"] = row


etiket = Label(text="Sorgunuzu giriniz : ")
etiket.pack()

area = Text()
area.config(width=50, height=10, font="arial 12")
area.pack()

etiket2 = Label(text=" ")
etiket2.pack()

etiket3 = Label(text=" ")
etiket3.pack()

sorgulama = Button(text="Sorgula", command=Sorgula)
sorgulama.pack()

mainloop()