from cProfile import label
from cgitb import text
import datetime
from email.mime import image
from logging import root
from string import whitespace
import string
import stringprep
from tkinter import*
from tkinter import ttk
from tkinter import font
from turtle import title, update, width
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import date




class Face_recognition():
   def __init__(self,root):
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("Face Recognition System")

      title_lbl=Label(self.root,text="FACE RECOGNITION",font=("Helvetica",30,"bold"),bg="aqua",fg="red")
      title_lbl.place(x=0,y=0,width=1300,height=45)

      img_top=Image.open(r"Face attendance images\facial-recognition-connected-real-estate.png")
      img_top=img_top.resize((570,610),Image.ANTIALIAS)
      self.photoimg_top=ImageTk.PhotoImage(img_top)

      f_lbl=Label(self.root,image=self.photoimg_top)
      f_lbl.place(x=0,y=47,width=570,height=610)

      
      img_bottom=Image.open(r"Face attendance images\facescanningldng.webp")
      img_bottom=img_bottom.resize((715,610),Image.ANTIALIAS)
      self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

      f_lbl=Label(self.root,image=self.photoimg_bottom)
      f_lbl.place(x=570,y=47,width=715,height=610)

      #btn
      b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",14,"bold","italic"),bg="yellow",fg="black")
      b1_1.place(x=260,y=534,width=180,height=40)

      # ============== Attendance ================
      def mark_attendance(self,r,n,d):
         with open("group.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
               entry=line.split((","))
               name_list.append(entry[0])
            if((r not in name_list) and (n not in name_list) and (d not in name_list)):
               now=datetime.now()
               d1=now.strftime("%d/%m/%Y")
               dtString=now.strftime("%H:%M:%S")
               f.writelines(f"\n{r},{n},{d},{dtString},{d1},present")



      





      


      # ============== face Recog =================
   def face_recog(self):
         def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
           gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
           features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

           coord=[]

           for (x,y,w,h) in features:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
            id,predict=clf.predict(gray_image[y:y+h,x:x+w])
            confidence=int((100*(1-predict/300)))

            conn=mysql.connector.connect(host="localhost",username="root",password="2002",database="face_recognizer")
            my_cursor=conn.cursor()

            my_cursor.execute("select Name from student where Std_id="+str(id))
            n=my_cursor.fetchone()
            n="+".join(n)

            my_cursor.execute("select RollNo from student where Std_id="+str(id))
            r=my_cursor.fetchone()
            r="+".join(r)

            my_cursor.execute("select Dep from student where Std_id="+str(id))
            d=my_cursor.fetchone()
            d="+".join(d)



            if confidence>77:
               # cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
               cv2.putText(img,f"RollNo:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
               cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
               cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
               self.mark_attendance(r,n,d)
            else:
               cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
               cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

               coord=[x,y,w,h]
            return coord
         
         def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

         faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
         clf = cv2.face.LBPHFaceRecognizer_create()
         clf.read("classifier.xml")

         video_cap=cv2.VideoCapture(0)

         while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
               break
            video_cap.release()
            cv2.destroyAllWindows()

         




             
      

      


         

         








if __name__== "__main__":
   root=Tk()
   obj=Face_recognition(root)
   root.mainloop()