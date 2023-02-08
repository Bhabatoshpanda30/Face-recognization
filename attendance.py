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
import csv
from tkinter import filedialog as fd


mydata=[]
class Attendance:
   def __init__(self,root):
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("Face Recognition System")


      # First image
      img_top=Image.open(r"Face attendance images\pp.jpg")
      img_top=img_top.resize((650,170),Image.ANTIALIAS)
      self.photoimg_top=ImageTk.PhotoImage(img_top)

      f_lbl=Label(self.root,image=self.photoimg_top)
      f_lbl.place(x=0,y=0,width=650,height=170)

      # Second image
      img_bottom=Image.open(r"Face attendance images\classes.jpg")
      img_bottom=img_bottom.resize((650,170),Image.ANTIALIAS)
      self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

      f_lbl=Label(self.root,image=self.photoimg_bottom)
      f_lbl.place(x=645,y=0,width=650,height=170)

      title_lbl=Label(self.root,text="ATTENDANCE MANAGEMENT SYSTEM",font=("Helvetica",30,"bold"),bg="light yellow",fg="dark cyan")
      title_lbl.place(x=0,y=170,width=1300,height=45)

      # bg img
      img3=Image.open(r"C:\Users\bhaba\Downloads\FACE RECOGNIZATION\Face attendance images\bgggg.jpg")
      img3=img3.resize((1350,510),Image.ANTIALIAS)
      self.photoimg3=ImageTk.PhotoImage(img3)

      bg_img=Label(self.root,image=self.photoimg3)
      bg_img.place(x=0,y=215,width=1350,height=510)

      main_frame=Frame(bg_img,bd=2,bg="white")
      main_frame.place(x=0,y=4,width=1400,height=600)

       # left label frame
      Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
      Left_frame.place(x=7,y=0.5,width=625,height=415.5)

      img_left=Image.open(r"C:\Users\bhaba\Downloads\FACE RECOGNIZATION\Face attendance images\attndtkn.jpg")
      img_left=img_left.resize((615,130),Image.ANTIALIAS)
      self.photoimg_left=ImageTk.PhotoImage(img_left)

      f_lbl=Label(Left_frame,image=self.photoimg_left)
      f_lbl.place(x=5,y=0,width=615,height=100)

      left_inside_frame=Frame(main_frame,bd=2,relief=RIDGE,bg="white")
      left_inside_frame.place(x=12,y=125,width=615,height=290)

      # lable and entry
      # attndence Id 
      attendanceId_label=Label(left_inside_frame,text="AttendanceID:",font=("times new roman",11,"bold"),width=10,bg="white")
      attendanceId_label.grid(row=0,column=0,padx=7,pady=7,sticky=W)

      attendanceId_entry=ttk.Entry(left_inside_frame,width=22,font=("times new roman",10,"bold"))
      attendanceId_entry.grid(row=0,column=1,padx=7,pady=7,sticky=W)

      # roll
      rollLable_label=Label(left_inside_frame,text="Roll:",font=("times new roman",11,"bold"),width=10,bg="white")
      rollLable_label.grid(row=0,column=2,padx=7,pady=7,sticky=W)

      atten_roll_entry=ttk.Entry(left_inside_frame,width=22,font=("times new roman",10,"bold"))
      atten_roll_entry.grid(row=0,column=3,padx=7,pady=7,sticky=W)

      # name
      nameLable_label=Label(left_inside_frame,text="Name:",font=("times new roman",11,"bold"),width=10,bg="white")
      nameLable_label.grid(row=1,column=0,padx=7,pady=8,sticky=W)

      atten_name_entry=ttk.Entry(left_inside_frame,width=22,font=("times new roman",10,"bold"))
      atten_name_entry.grid(row=1,column=1,padx=7,pady=8,sticky=W)

      # dep
      depLable_label=Label(left_inside_frame,text="Department:",font=("times new roman",11,"bold"),width=10,bg="white")
      depLable_label.grid(row=1,column=2,padx=7,pady=7,sticky=W)

      atten_dep_entry=ttk.Entry(left_inside_frame,width=22,font=("times new roman",10,"bold"))
      atten_dep_entry.grid(row=1,column=3,padx=7,pady=7,sticky=W)

      # time
      timeLable_label=Label(left_inside_frame,text="Time:",font=("times new roman",11,"bold"),width=10,bg="white")
      timeLable_label.grid(row=2,column=0,padx=7,pady=8,sticky=W)

      atten_time_entry=ttk.Entry(left_inside_frame,width=22,font=("times new roman",10,"bold"))
      atten_time_entry.grid(row=2,column=1,padx=7,pady=8,sticky=W)

      # date
      dateLable_label=Label(left_inside_frame,text="Date:",font=("times new roman",11,"bold"),width=10,bg="white")
      dateLable_label.grid(row=2,column=2,padx=7,pady=7,sticky=W)

      atten_date_entry=ttk.Entry(left_inside_frame,width=22,font=("times new roman",10,"bold"))
      atten_date_entry.grid(row=2,column=3,padx=7,pady=7,sticky=W)

      # attendance status
      attendancee_label=Label(left_inside_frame,text="Attndc Status:",font=("times new roman",11,"bold"),width=10,bg="white")
      attendancee_label.grid(row=3,column=0)

      
      self.attendancee_label_status=ttk.Combobox(left_inside_frame,font=("comicsansns",10,"bold"),width=22,state="readonly")
      self.attendancee_label_status["values"]=("Status","Present","Absent")
      self.attendancee_label_status.current(0)
      self.attendancee_label_status.grid(row=3,column=1,pady=8)

      # button frame
      btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
      btn_frame.place(x=1,y=245,width=610,height=30)

      save_btn=Button(btn_frame,text="Import Csv",command=self.importCsv,width=21,font=("times new roman",9,"bold"),bg="blue",fg="white")
      save_btn.grid(row=0,column=0)

      update_btn=Button(btn_frame,text="Export csv",width=21,font=("times new roman",9,"bold"),bg="blue",fg="white")
      update_btn.grid(row=0,column=1)

      delete_btn=Button(btn_frame,text="Update",width=20,font=("times new roman",9,"bold"),bg="blue",fg="white")
      delete_btn.grid(row=0,column=2)

      reset_btn=Button(btn_frame,text="Reset",width=20,font=("times new roman",9,"bold"),bg="blue",fg="white")
      reset_btn.grid(row=0,column=3)




      # Right label frame
      Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
      Right_frame.place(x=640,y=0.5,width=625,height=415.5)

      table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
      table_frame.place(x=2,y=1,width=617,height=393)

      # ================= scroll bar table =================
      # table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
      # table_frame.place(x=3,y=5,width=615,height=390)

      scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
      scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
      self.AttendanceReport_table=ttk.Treeview(table_frame,column=("Id","Roll","Name","Department","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) 

      scroll_x.pack(side=BOTTOM,fill=X)
      scroll_y.pack(side=RIGHT,fill=Y)
      scroll_x.config(command=self.AttendanceReport_table.xview)
      scroll_y.config(command=self.AttendanceReport_table.yview)

      self.AttendanceReport_table.heading("Id",text="Attendance Id")
      self.AttendanceReport_table.heading("Roll",text="Roll")
      self.AttendanceReport_table.heading("Name",text="Name")
      self.AttendanceReport_table.heading("Department",text="Department")
      self.AttendanceReport_table.heading("Time",text="Time")
      self.AttendanceReport_table.heading("Date",text="Date")
      self.AttendanceReport_table.heading("Attendance",text="Attendance")
      self.AttendanceReport_table["show"]="headings"

      self.AttendanceReport_table.column("Id",width=100)
      self.AttendanceReport_table.column("Roll",width=100)
      self.AttendanceReport_table.column("Name",width=100)
      self.AttendanceReport_table.column("Department",width=100)
      self.AttendanceReport_table.column("Time",width=100)
      self.AttendanceReport_table.column("Date",width=100)
      self.AttendanceReport_table.column("Attendance",width=100)

      self.AttendanceReport_table.pack(fill=BOTH,expand=0.5)

      #=============== fetch data =====================

   def fetchData(self,rows):
      self.AttendanceReport_table.delete(*self.AttendanceReport_table.get_children())
      for i in rows:
         self.AttendanceReport_table.insert("",END,values=i)

   def importCsv(self):
      global mydata
      fln=fd.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*" )),parent=self.root)
      with open(fln) as myfile:
         csvread=csv.reader(myfile,delimiter=",")
         for i in csvread:
            mydata.append(i)
         self.fetchData(mydata)



      
         








     

      





if __name__== "__main__":
   root=Tk()
   obj=Attendance(root)
   root.mainloop()
