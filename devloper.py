from cProfile import label
from cgitb import text
from email.mime import image
from logging import root
from string import whitespace
import string
from tkinter import*
from tkinter import ttk
from tkinter import font
from turtle import title, update, width
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os



class Devloper():
   def __init__(self,root):
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("Face Recognition System")

      title_lbl=Label(self.root,text="DEVLOPER",font=("Palatino",30,"bold","italic"),bg="blue",fg="yellow")
      title_lbl.place(x=0,y=0,width=1300,height=45)

      img_top=Image.open(r"Face attendance images\dev.jpg")
      img_top=img_top.resize((1300,630),Image.ANTIALIAS)
      self.photoimg_top=ImageTk.PhotoImage(img_top)

      f_lbl=Label(self.root,image=self.photoimg_top)
      f_lbl.place(x=0,y=47,width=1300,height=630)

      main_frame=Frame(f_lbl,bd=2,bg="white")
      main_frame.place(x=660,y=0,width=650,height=550)


      img_top1=Image.open(r"Face attendance images\me.jpeg")
      img_top1=img_top1.resize((220,200),Image.ANTIALIAS)
      self.photoimg_top1=ImageTk.PhotoImage(img_top1)

      f_lbl=Label(main_frame,image=self.photoimg_top1)
      f_lbl.place(x=0,y=50,width=220,height=200)

      img_top2=Image.open(r"Face attendance images\manishi.jpeg")
      img_top2=img_top2.resize((190,200),Image.ANTIALIAS)
      self.photoimg_top2=ImageTk.PhotoImage(img_top2)

      f_lbl=Label(main_frame,image=self.photoimg_top2)
      f_lbl.place(x=230,y=50,width=190,height=200)

      img_top3=Image.open(r"Face attendance images\ghumu.jpg")
      img_top3=img_top3.resize((180,200),Image.ANTIALIAS)
      self.photoimg_top3=ImageTk.PhotoImage(img_top3)

      f_lbl=Label(main_frame,image=self.photoimg_top3)
      f_lbl.place(x=430,y=50,width=180,height=200)


      dev_label=Label(main_frame,text="Hello All !!",font=("times new roman",13,"bold"),width=10,bg="cyan")
      dev_label.place(x=270,y=0)
      dev_label1=Label(main_frame,text="Welcome To The Devlopers Page",font=("times new roman",13,"bold"),width=30,bg="green",fg="yellow")
      dev_label1.place(x=180,y=20)

      dev_label=Label(main_frame,text="Bhabatosh Panda",font=("times new roman",13,"bold"),width=20,bg="white",fg="blue")
      dev_label.place(x=6,y=250)

      dev_label=Label(main_frame,text="Sk Md Samim Akhtar",font=("times new roman",13,"bold"),width=20,bg="white",fg="blue")
      dev_label.place(x=220,y=250)

      dev_label=Label(main_frame,text="Satyajeet Nath",font=("times new roman",13,"bold"),width=20,bg="white",fg="blue")
      dev_label.place(x=420,y=250)

      dev_label=Label(main_frame,text="(20CSE271)",font=("times new roman",13,"bold"),width=20,bg="white",fg="blue")
      dev_label.place(x=6,y=270)

      dev_label=Label(main_frame,text="(20CSE266)",font=("times new roman",13,"bold"),width=20,bg="white",fg="blue")
      dev_label.place(x=220,y=270)

      dev_label=Label(main_frame,text="(20CSE275)",font=("times new roman",13,"bold"),width=20,bg="white",fg="blue")
      dev_label.place(x=420,y=270)

      dev_label=Label(main_frame,text="HELP DESK",font=("times new roman",20,"bold"),width=30,bg="red",fg="yellow")
      dev_label.place(x=60,y=300)

      dev_label=Label(main_frame,text="Contact info :",font=("times new roman",15,"bold","italic"),width=17,bg="white")
      dev_label.place(x=210,y=340)

      dev_label=Label(main_frame,text="1. Bhabatosh :- Ph: 6371135984 , Email: bhabatoshpanda30@gmail.com",font=("times new roman",14,"bold","italic"),width=55,bg="white",fg="navy blue")
      dev_label.place(x=0,y=370)
      dev_label=Label(main_frame,text="2. Sk Md Samim :- Ph: 9668521910 , Email: skmdsamim786@gmail.com",font=("times new roman",14,"bold","italic"),width=55,bg="white",fg="navy blue")
      dev_label.place(x=0,y=400)
      dev_label=Label(main_frame,text="2. Satyajeet :- Ph: 7205169819 , Email: sjeet1781@gmail.com",font=("times new roman",14,"bold","italic"),width=55,bg="white",fg="navy blue")
      dev_label.place(x=0,y=430)

      dev_label=Label(main_frame,text="THANK YOU !!",font=("Wide Latin",22,"bold",),width=17,bg="white")
      dev_label.place(x=30,y=480)
    







if __name__== "__main__":
   root=Tk()
   obj=Devloper(root)
   root.mainloop()
