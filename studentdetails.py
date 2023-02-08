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



class Student():
   def __init__(self,root):
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("Face Recognition System")

      #=== variables ====
      self.var_dep=StringVar()
      self.var_course=StringVar()
      self.var_year=StringVar()
      self.var_semester=StringVar()
      self.var_std_id=StringVar()
      self.var_std_name=StringVar()
      self.var_div=StringVar()
      self.var_roll=StringVar()
      self.var_gender=StringVar()
      self.var_dob=StringVar()
      self.var_email=StringVar()
      self.var_phone=StringVar()
      self.var_adress=StringVar()
      self.var_teacher=StringVar()


      # First image
      img=Image.open(r"C:\Users\bhaba\Downloads\FACE RECOGNIZATION\Face attendance images\traind.jpg")
      img=img.resize((500,130),Image.ANTIALIAS)
      self.photoimg=ImageTk.PhotoImage(img)

      f_lbl=Label(self.root,image=self.photoimg)
      f_lbl.place(x=0,y=0,width=500,height=130)


      # Second image
      img1=Image.open(r"C:\Users\bhaba\Downloads\FACE RECOGNIZATION\Face attendance images\stdimgg2.jpg")
      img1=img1.resize((500,130),Image.ANTIALIAS)
      self.photoimg1=ImageTk.PhotoImage(img1)

      f_lbl=Label(self.root,image=self.photoimg1)
      f_lbl.place(x=500,y=0,width=400,height=130)

      # Third image
      img2=Image.open(r"C:\Users\bhaba\Downloads\FACE RECOGNIZATION\Face attendance images\stdimg3.jpg")
      img2=img2.resize((500,130),Image.ANTIALIAS)
      self.photoimg2=ImageTk.PhotoImage(img2)

      f_lbl=Label(self.root,image=self.photoimg2)
      f_lbl.place(x=900,y=0,width=500,height=130)

      # Background img
      img3=Image.open(r"C:\Users\bhaba\Downloads\FACE RECOGNIZATION\Face attendance images\stdbg2.jpg")
      img3=img3.resize((1350,510),Image.ANTIALIAS)
      self.photoimg3=ImageTk.PhotoImage(img3)

      bg_img=Label(self.root,image=self.photoimg3)
      bg_img.place(x=0,y=130,width=1350,height=610)

      title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("Palatino",30,"bold"),bg="blue",fg="yellow")
      title_lbl.place(x=0,y=0,width=1280,height=45)

      main_frame=Frame(bg_img,bd=2,bg="white")
      main_frame.place(x=0,y=60,width=1400,height=600)

      # left label frame
      Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
      Left_frame.place(x=10,y=10,width=610,height=580)

      # First image
      img_left=Image.open(r"C:\Users\bhaba\Downloads\FACE RECOGNIZATION\Face attendance images\csest.jpg")
      img_left=img_left.resize((600,130),Image.ANTIALIAS)
      self.photoimg_left=ImageTk.PhotoImage(img_left)

      f_lbl=Label(Left_frame,image=self.photoimg_left)
      f_lbl.place(x=5,y=0,width=600,height=80)

      # current course
      current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
      current_course_frame.place(x=5,y=75,width=600,height=100)

      # Department
      dep_label=Label(current_course_frame,text="Department",font=("times new roman",10,"bold"),width=10,bg="white")
      dep_label.grid(row=0,column=0,padx=7,sticky=W)

      dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),width=17,state="readonly")
      dep_combo["values"]=("Select Department","CSE","CST","Civil","Mechanical","BioTech","Electrical","Chemical","Electronics","Aerospace","Bsc Ag","MCA","BCA","BBA","MBA")
      dep_combo.current(0)
      dep_combo.grid(row=0,column=1,padx=1,pady=8,sticky=W)

      # Courses
      course_label=Label(current_course_frame,text="     Courses",font=("times new roman",10,"bold"),width=9,bg="white")
      course_label.grid(row=0,column=2,padx=7,sticky=W)

      course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",10,"bold"),width=17,state="readonly")
      course_combo["values"]=("Select Course","BE/Btech","Management Studies","Bsc","Technical")
      course_combo.current(0)
      course_combo.grid(row=0,column=3,padx=1,pady=8,sticky=W)

      # Year
      year_label=Label(current_course_frame,text="Year",font=("times new roman",10,"bold"),width=10,bg="white")
      year_label.grid(row=1,column=0,padx=7,sticky=W)

      year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",10,"bold"),width=17,state="readonly")
      year_combo["values"]=("Select Year","2018-22","2019-23","2020-24","2021-25","2022-26")
      year_combo.current(0)
      year_combo.grid(row=1,column=1,padx=1,pady=8,sticky=W)

      # semester
      semester_label=Label(current_course_frame,text="Semester",font=("times new roman",10,"bold"),width=10,bg="white")
      semester_label.grid(row=1,column=2,padx=7,sticky=W)

      semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",10,"bold"),width=17,state="readonly")
      semester_combo["values"]=("Select Semester","Sem-1","Sem-2","Sem-3","Sem-4","Sem-5","Sem-6","Sem-7","Sem-8")
      semester_combo.current(0)
      semester_combo.grid(row=1,column=3,padx=1,pady=8,sticky=W)

       # class student information
      class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
      class_student_frame.place(x=5,y=175,width=600,height=246)

       # student Id 
      studentId_label=Label(class_student_frame,text="StudentID:",font=("times new roman",9,"bold"),width=10,bg="white")
      studentId_label.grid(row=0,column=0,padx=7,sticky=W)

      studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=18,font=("times new roman",9,"bold"))
      studentID_entry.grid(row=0,column=1,padx=7,sticky=W)

      # student Name 
      studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",9,"bold"),width=10,bg="white")
      studentName_label.grid(row=0,column=2,padx=7,pady=5,sticky=W)

      studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",9,"bold"))
      studentName_entry.grid(row=0,column=3,padx=7,pady=5,sticky=W)

      # class division
      class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",9,"bold"),width=10,bg="white")
      class_div_label.grid(row=1,column=0,padx=7,pady=5,sticky=W)


      division_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",10,"bold"),width=17,state="readonly")
      division_combo["values"]=("Select division","A","B","C","D","E","F","G","H","I","J")
      division_combo.current(0)
      division_combo.grid(row=1,column=1,padx=8,pady=8,sticky=W)

      # roll no
      roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",9,"bold"),width=10,bg="white")
      roll_no_label.grid(row=1,column=2,padx=7,pady=5,sticky=W)

      roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",9,"bold"))
      roll_no_entry.grid(row=1,column=3,padx=7,pady=5,sticky=W)


      # Gender
      gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",9,"bold"),width=10,bg="white")
      gender_label.grid(row=2,column=0,padx=7,pady=5,sticky=W)

      
      gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",10,"bold"),width=17,state="readonly")
      gender_combo["values"]=("Select gender","Male","Female","Prefer Not Say")
      gender_combo.current(0)
      gender_combo.grid(row=2,column=1,padx=8,pady=8,sticky=W)

      # DOB
      dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",9,"bold"),width=10,bg="white")
      dob_label.grid(row=2,column=2,padx=7,pady=5,sticky=W)

      dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",9,"bold"))
      dob_entry.grid(row=2,column=3,padx=7,pady=5,sticky=W)

       # Phone
      phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",9,"bold"),width=10,bg="white")
      phone_label.grid(row=3,column=0,padx=7,pady=5,sticky=W)

      phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=18,font=("times new roman",9,"bold"))
      phone_entry.grid(row=3,column=1,padx=7,pady=5,sticky=W)

      # email
      email_label=Label(class_student_frame,text="Email:",font=("times new roman",9,"bold"),width=10,bg="white")
      email_label.grid(row=3,column=2,padx=7,pady=5,sticky=W)

      email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",9,"bold"))
      email_entry.grid(row=3,column=3,padx=7,pady=5,sticky=W)

      # adress
      adress_label=Label(class_student_frame,text="Adress:",font=("times new roman",9,"bold"),width=10,bg="white")
      adress_label.grid(row=4,column=0,padx=7,pady=5,sticky=W)

      adress_entry=ttk.Entry(class_student_frame,textvariable=self.var_adress,width=18,font=("times new roman",9,"bold"))
      adress_entry.grid(row=4,column=1,padx=7,pady=5,sticky=W)

      # Teacher Name
      teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",9,"bold"),width=10,bg="white")
      teacher_label.grid(row=4,column=2,padx=7,pady=5,sticky=W)

      teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",9,"bold"))
      teacher_entry.grid(row=4,column=3,padx=7,pady=5,sticky=W)
      # radio btn
      self.var_radio1=StringVar()
      radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
      radiobtn1.grid(row=5,column=0)

      self.var_radio2=StringVar()
      radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
      radiobtn2.grid(row=5,column=1)

      # button frame
      btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
      btn_frame.place(x=0,y=185,width=590,height=30)

      save_btn=Button(btn_frame,text="Save",command=self.add_data,width=10,font=("times new roman",9,"bold"),bg="blue",fg="white")
      save_btn.grid(row=0,column=0)

      update_btn=Button(btn_frame,text="Update",width=10,command=self.Update_data,font=("times new roman",9,"bold"),bg="blue",fg="white")
      update_btn.grid(row=0,column=1)

      delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=10,font=("times new roman",9,"bold"),bg="blue",fg="white")
      delete_btn.grid(row=0,column=2)

      reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=10,font=("times new roman",9,"bold"),bg="blue",fg="white")
      reset_btn.grid(row=0,column=3)

      takea_photo_btn=Button(btn_frame,text="Take Photo Sample",command=self.generate_dataset,width=19,font=("times new roman",9,"bold"),bg="blue",fg="white")
      takea_photo_btn.grid(row=0,column=4)

      update_photo_btn=Button(btn_frame,text="Update Photo Sample",width=18,font=("times new roman",9,"bold"),bg="blue",fg="white")
      update_photo_btn.grid(row=0,column=5)









      # Right label frame
      Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
      Right_frame.place(x=640,y=10,width=610,height=580)

      # First image
      img_right=Image.open(r"C:\Users\bhaba\Downloads\FACE RECOGNIZATION\Face attendance images\stdtls.jpg")
      img_right=img_right.resize((600,130),Image.ANTIALIAS)
      self.photoimg_right=ImageTk.PhotoImage(img_right)

      f_lbl=Label(Right_frame,image=self.photoimg_right)
      f_lbl.place(x=5,y=0,width=600,height=80)

      #   ====  searching system  ====
      search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System:",font=("times new roman",12,"bold"))
      search_frame.place(x=5,y=72,width=601,height=57)

      search_label=Label(search_frame,text="Search By:",font=("times new roman",9,"bold"),width=10,bg="aqua")
      search_label.grid(row=0,column=0,padx=7,pady=5,sticky=W)

      search_combo=ttk.Combobox(search_frame,font=("times new roman",10,"bold"),width=17,state="readonly")
      search_combo["values"]=("Select","Roll_No","Phone_No")
      search_combo.current(0)
      search_combo.grid(row=0,column=1,padx=1,pady=8,sticky=W)

      search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",9,"bold"))
      search_entry.grid(row=0,column=2,padx=7,pady=5,sticky=W)

      search_btn=Button(search_frame,text="Search",width=13,font=("times new roman",9,"bold"),bg="blue",fg="white")
      search_btn.grid(row=0,column=3,padx=6)

      showAll_btn=Button(search_frame,text="Show All",width=13,font=("times new roman",9,"bold"),bg="blue",fg="white")
      showAll_btn.grid(row=0,column=4)

     # ====   table frame   ====
      table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
      table_frame.place(x=5,y=130,width=601,height=285)

      scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
      scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
      self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","adress","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) 

      scroll_x.pack(side=BOTTOM,fill=X)
      scroll_y.pack(side=RIGHT,fill=Y)
      scroll_x.config(command=self.student_table.xview)
      scroll_y.config(command=self.student_table.yview)


      self.student_table.heading("dep",text="Department")
      self.student_table.heading("course",text="Course")
      self.student_table.heading("year",text="Year")
      self.student_table.heading("sem",text="Semester")
      self.student_table.heading("id",text="Student Id")
      self.student_table.heading("name",text="Name")
      self.student_table.heading("div",text="Division")
      self.student_table.heading("roll",text="Roll No")
      self.student_table.heading("gender",text="Gender")
      self.student_table.heading("dob",text="DOB")
      self.student_table.heading("email",text="Email")
      self.student_table.heading("phone",text="Phone")
      self.student_table.heading("adress",text="Adress")
      self.student_table.heading("teacher",text="Teacher")
      self.student_table.heading("photo",text="PhotoSampleStatus")
      self.student_table["show"]="headings"
     

      self.student_table.column("dep",width=100)
      self.student_table.column("course",width=100)
      self.student_table.column("year",width=100)
      self.student_table.column("sem",width=100)
      self.student_table.column("id",width=100)
      self.student_table.column("name",width=100)
      self.student_table.column("div",width=100)
      self.student_table.column("roll",width=100)
      self.student_table.column("gender",width=100)
      self.student_table.column("dob",width=100)
      self.student_table.column("email",width=100)
      self.student_table.column("phone",width=100)
      self.student_table.column("adress",width=100)
      self.student_table.column("teacher",width=100)
      self.student_table.column("photo",width=150)
      

      self.student_table.pack(fill=BOTH,expand=0.5)
      self.student_table.bind("<ButtonRelease>",self.get_cursor)
      self.fetch_data()

   #========== function declaration ===========
   def add_data(self):
      if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
         messagebox.showerror("Error","All fields are required",parent=self.root)
      else:
          try:
               conn=mysql.connector.connect(host="localhost",username="root",password="2002",database="face_recognizer")
               my_cursor=conn.cursor()
               my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                               self.var_dep.get(),
                                                                                                               self.var_course.get(),
                                                                                                               self.var_year.get(),
                                                                                                               self.var_semester.get(),
                                                                                                               self.var_std_id.get(),
                                                                                                               self.var_std_name.get(),
                                                                                                               self.var_div.get(),
                                                                                                               self.var_roll.get(),
                                                                                                               self.var_gender.get(),
                                                                                                               self.var_dob.get(),
                                                                                                               self.var_email.get(),
                                                                                                               self.var_phone.get(),
                                                                                                               self.var_adress.get(),
                                                                                                               self.var_teacher.get(),
                                                                                                               self.var_radio1.get()

                                                                                                             ))
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
          except Exception as es:
               messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)


   #===== fetch data =======
   def fetch_data(self):
      conn=mysql.connector.connect(host="localhost",username="root",password="2002",database="face_recognizer")
      my_cursor=conn.cursor()
      my_cursor.execute("select * from student")
      data=my_cursor.fetchall()

      if len(data)!=0:
         self.student_table.delete(*self.student_table.get_children())
         for i in data:
            self.student_table.insert("",END,values=i)
         conn.commit()
      conn.close()

  

   #=========== get cursor ==========
   def get_cursor(self,event=""):
      cursor_focus=self.student_table.focus()
      content=self.student_table.item(cursor_focus)
      data=content["values"]

      self.var_dep.set(data[0]),
      self.var_course.set(data[1]),
      self.var_year.set(data[2]),
      self.var_semester.set(data[3]),
      self.var_std_id.set(data[4]),
      self.var_std_name.set(data[5]),
      self.var_div.set(data[6]),
      self.var_roll.set(data[7]),
      self.var_gender.set(data[8]),
      self.var_dob.set(data[9]),
      self.var_email.set(data[10]),
      self.var_phone.set(data[11]),
      self.var_adress.set(data[12]),
      self.var_teacher.set(data[13]),
      self.var_radio1.set(data[14])

   # update function
   # update function
   def Update_data(self):
      if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
         messagebox.showerror("Error","All fields are required",parent=self.root)
      else:
         try:
            Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
            if Update>0:
               conn=mysql.connector.connect(host="localhost",username="root",password="2002",database="face_recognizer")
               my_cursor=conn.cursor()
           
            
               stmt = "Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,RollNo=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Adress=%s,Teacher=%s,PhotoSample=%s where Std_id=%s;"
               my_cursor.execute("Update student set "+ stmt,(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_adress.get(),self.var_teacher.get(),self.var_radio1.get(),self.var_std_id.get()))

               conn.commit()
               conn.close()
            else:
               if not Update:
                  return
            messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
            conn.commit()
            self.fetch_data()
            conn.close()
         except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
  

   # delete function
   def delete_data(self):
      if self.var_std_id.get()=="":
         messagebox.showerror("Error", "Student id must be required",parent=self.root)
      else:
         try:
            delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
            if delete>0:
               conn=mysql.connector.connect(host="localhost",username="root",password="2002",database="face_recognizer")
               my_cursor=conn.cursor()
               sql="delete from student where Std_id=%s"
               val=(self.var_std_id.get(),)
               my_cursor.execute(sql,val)
            else:
               if not delete:
                  return
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
         except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

   # reset function
   def reset_data(self):
      self.var_dep.set("Select Department")
      self.var_course.set("Select course")
      self.var_year.set("Select Year")
      self.var_semester.set("Select Semester")
      self.var_std_id.set("")
      self.var_std_name.set("")
      self.var_div.set("Select Division")
      self.var_roll.set("")
      self.var_gender.set("Select Gender")
      self.var_dob.set("")
      self.var_email.set("")
      self.var_phone.set("")
      self.var_adress.set("")
      self.var_teacher.set("")
      self.var_radio1.set("")

   #  ======== Generte data set or Take photo Sample ===============
   def generate_dataset(self):
      if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
         messagebox.showerror("Error","All fields are required",parent=self.root)
      else:
         try:
               conn=mysql.connector.connect(host="localhost",username="root",password="2002",database="face_recognizer")
               my_cursor=conn.cursor()
               my_cursor.execute("select * from student")
               myresult=my_cursor.fetchall()
               id=0
               for x in myresult:
                  id+=1
               my_cursor.execute('Update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,RollNo=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Adress=%s,Teacher=%s,PhotoSample=%s where Std_id=%s',(
                                                                                                                                                                       
                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                                                
                                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                self.var_adress.get(),
                                                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                self.var_std_id.get()==id+1
                                                                                                                                                                                                            ))
               conn.commit()  
               self.fetch_data()
               self.reset_data()
               conn.close()


  
         # ========== Load predefiend data on face frontals from opencv ============
               face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

               def face_cropped(img):
                  gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                  faces=face_classifier.detectMultiScale(gray,1.3,5)
                  #scaling factor=1.3
                  #minimum Neighbor=5

                  for (x,y,w,h) in faces:
                     face_cropped=img[y:y+h,x:x+w]
                     return face_cropped

               cap=cv2.VideoCapture(0)
               img_id=0
               while True:
                  ret,my_frame=cap.read()
                  if face_cropped(my_frame) is not None:
                     img_id+=1

                  face=cv2.resize(face_cropped(my_frame),(450,450))
                  face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

                  file_name_path="IMG_data/user."+str(id)+"."+str(img_id)+".jpg"
                  filename = "user."+str(id)+"."+str(img_id)+".jpg"
                  cv2.imwrite(file_name_path,face)

                  cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                  cv2.imshow("Cropped Face",face)

                  if cv2.waitKey(2)==13 or int(img_id)==20:
                     break
               cap.release()
               cv2.destroyAllWindows()
               messagebox.showinfo("Result","Generating data sets completed!!")
         except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)




      
               



            
               





            





         
                                                                                                                                                                                           
                                                                                                                                                                            
                                                                                                                                                                        

        
      


               

                    
      
         


   
   
  


      













if __name__== "__main__":
   root=Tk()
   obj=Student(root)
   root.mainloop()