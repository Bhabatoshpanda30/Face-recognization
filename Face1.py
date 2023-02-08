from cProfile import label
from cgitb import text
from email.mime import image
from msilib.schema import SelfReg
from tkinter import*
from tkinter import ttk
from tkinter import font
import tkinter
from turtle import title, width
from typing import Self
from PIL import Image, ImageTk
from studentdetails import Student
import os
from train import Train
from face_recog import Face_recognition
from attendance import Attendance
from devloper import Devloper
from chatbot import Chatbot


class Face_Recognition_System():
   def __init__(self,root):
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("Face Recognition System")

      # First image
      img=Image.open(r"C:\Users\bhaba\Downloads\FACE RECOGNIZATION\Face attendance images\giet-university.jpg")
      img=img.resize((500,130),Image.ANTIALIAS)
      self.photoimg=ImageTk.PhotoImage(img)

      f_lbl=Label(self.root,image=self.photoimg)
      f_lbl.place(x=0,y=0,width=500,height=130)


      # Second image
      img1=Image.open(r"C:\Users\bhaba\Downloads\FACE RECOGNIZATION\Face attendance images\face.jpeg")
      img1=img1.resize((500,130),Image.ANTIALIAS)
      self.photoimg1=ImageTk.PhotoImage(img1)

      f_lbl=Label(self.root,image=self.photoimg1)
      f_lbl.place(x=500,y=0,width=400,height=130)

      # Third image
      img2=Image.open(r"C:\Users\bhaba\Downloads\FACE RECOGNIZATION\Face attendance images\guest-house.jpg")
      img2=img2.resize((500,130),Image.ANTIALIAS)
      self.photoimg2=ImageTk.PhotoImage(img2)

      f_lbl=Label(self.root,image=self.photoimg2)
      f_lbl.place(x=900,y=0,width=500,height=130)


      # Background img
      img3=Image.open(r"C:\Users\bhaba\Downloads\FACE RECOGNIZATION\Face attendance images\bg6.jpg")
      img3=img3.resize((1350,510),Image.ANTIALIAS)
      self.photoimg3=ImageTk.PhotoImage(img3)

      bg_img=Label(self.root,image=self.photoimg3)
      bg_img.place(x=0,y=130,width=1350,height=610)

      title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("Palatino",30,"bold"),bg="white",fg="red")
      title_lbl.place(x=0,y=0,width=1270,height=45)

      # student btn
      img4=Image.open(r"C:\Users\bhaba\Downloads\FACE RECOGNIZATION\Face attendance images\laptop_college.jpg")
      img4=img4.resize((180,180),Image.ANTIALIAS)
      self.photoimg4=ImageTk.PhotoImage(img4)

      b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
      b1.place(x=100,y=70,width=180,height=180)

      b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("Lato",12,"bold"),bg="yellow",fg="dark blue")
      b1_1.place(x=100,y=200,width=180,height=50)

      # detect btn 2
      img5=Image.open(r"C:\Users\bhaba\Downloads\FACE RECOGNIZATION\Face attendance images\faced.jpg")
      img5=img5.resize((180,180),Image.ANTIALIAS)
      self.photoimg5=ImageTk.PhotoImage(img5)

      b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
      b1.place(x=400,y=70,width=180,height=180)

      b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("Lato",12,"bold"),bg="yellow",fg="dark blue")
      b1_1.place(x=400,y=200,width=180,height=50)

      # attendance btn 3
      img6=Image.open(r"C:\Users\bhaba\Downloads\FACE RECOGNIZATION\Face attendance images\imageat.jpg")
      img6=img6.resize((180,180),Image.ANTIALIAS)
      self.photoimg6=ImageTk.PhotoImage(img6)

      b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
      b1.place(x=700,y=70,width=180,height=180)

      b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("Lato",12,"bold"),bg="yellow",fg="dark blue")
      b1_1.place(x=700,y=200,width=180,height=50)

      # chatbot btn 4
      img7=Image.open(r"C:\Users\bhaba\Downloads\FACE RECOGNIZATION\Face attendance images\bot.webp")
      img7=img7.resize((180,180),Image.ANTIALIAS)
      self.photoimg7=ImageTk.PhotoImage(img7)

      b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.chatbot_data)
      b1.place(x=1000,y=70,width=180,height=180)

      b1_1=Button(bg_img,text="Chat bot",cursor="hand2",command=self.chatbot_data,font=("Lato",12,"bold"),bg="yellow",fg="dark blue")
      b1_1.place(x=1000,y=200,width=180,height=50)

      # tarin face btn 5
      img8=Image.open(r"C:\Users\bhaba\Downloads\FACE RECOGNIZATION\Face attendance images\images.jpg")
      img8=img8.resize((180,180),Image.ANTIALIAS)
      self.photoimg8=ImageTk.PhotoImage(img8)

      b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
      b1.place(x=100,y=300,width=180,height=180)

      b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("Lato",12,"bold"),bg="yellow",fg="dark blue")
      b1_1.place(x=100,y=430,width=180,height=50)

      # Photos face btn 6
      img9=Image.open(r"C:\Users\bhaba\Downloads\FACE RECOGNIZATION\Face attendance images\phts.jpg")
      img9=img9.resize((180,180),Image.ANTIALIAS)
      self.photoimg9=ImageTk.PhotoImage(img9)

      b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
      b1.place(x=400,y=300,width=180,height=180)

      b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("Lato",12,"bold"),bg="yellow",fg="dark blue")
      b1_1.place(x=400,y=430,width=180,height=50)

      # Devloper & help face btn 7
      img10=Image.open(r"C:\Users\bhaba\Downloads\FACE RECOGNIZATION\Face attendance images\hck2.jpg")
      img10=img10.resize((180,180),Image.ANTIALIAS)
      self.photoimg10=ImageTk.PhotoImage(img10)

      b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.devloper_data)
      b1.place(x=700,y=300,width=180,height=180)

      b1_1=Button(bg_img,text="Devloper & Help",cursor="hand2",command=self.devloper_data,font=("Lato",12,"bold"),bg="yellow",fg="dark blue")
      b1_1.place(x=700,y=430,width=180,height=50)

      # exit face btn 8
      img11=Image.open(r"C:\Users\bhaba\Downloads\FACE RECOGNIZATION\Face attendance images\exit.jpg")
      img11=img11.resize((180,180),Image.ANTIALIAS)
      self.photoimg11=ImageTk.PhotoImage(img11)

      b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
      b1.place(x=1000,y=300,width=180,height=180)

      b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("Lato",12,"bold"),bg="yellow",fg="dark blue")
      b1_1.place(x=1000,y=430,width=180,height=50)

   def open_img(self):
      os.startfile("IMG_data")

   def iExit(self):
       self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you Sure Exit This Project",parent=self.root)
    #    if Self.iExit >0:
    #     Self.root.destroy()
    #    else:
    #     return

    

      #= = = = functions btn = = = =
   def student_details(self):
       self.new_window=Toplevel(self.root)
       self.app=Student(self.new_window)

   def train_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Train(self.new_window)

   def face_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Face_recognition(self.new_window)

   def attendance_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Attendance(self.new_window)

   def devloper_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Devloper(self.new_window)

   def chatbot_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Chatbot(self.new_window)

   


      
   

            


      





if __name__ == "__main__":
   root=Tk()
   obj=Face_Recognition_System(root)
   root.mainloop()
