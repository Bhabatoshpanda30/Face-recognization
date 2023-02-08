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
import numpy as np



class Train():
   def __init__(self,root):
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("Face Recognition System")

      title_lbl=Label(self.root,text="TRAIN DATA SET",font=("Palatino",30,"bold"),bg="cyan",fg="red")
      title_lbl.place(x=0,y=0,width=1300,height=45)

      img_top=Image.open(r"Face attendance images\Working-of-Deep-Learning-in-Face-Recognition.jpg")
      img_top=img_top.resize((1300,280),Image.ANTIALIAS)
      self.photoimg_top=ImageTk.PhotoImage(img_top)

      f_lbl=Label(self.root,image=self.photoimg_top)
      f_lbl.place(x=0,y=47,width=1300,height=280)

      b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("Garamond",27,"bold","italic"),bg="light blue",fg="black")
      b1_1.place(x=0,y=320,width=1300,height=60)

      img_bottom=Image.open(r"Face attendance images\facetrain2.jpg")
      img_bottom=img_bottom.resize((1300,280),Image.ANTIALIAS)
      self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

      f_lbl=Label(self.root,image=self.photoimg_bottom)
      f_lbl.place(x=0,y=374,width=1300,height=280)



   def train_classifier(self):
      data_dir=("IMG_data")
      path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
   
      faces=[]
      ids=[]

      for image in path:
         img=Image.open(image).convert('L') #gray scale
         imageNp=np.array(img,'uint8')
         id=int(os.path.split(image)[1].split('.')[1])

         faces.append(imageNp)
         ids.append(id)
         cv2.imshow("Training",imageNp)
         cv2.waitKey(1)==13
      ids=np.array(ids)

      #====== Train the clasifier and save ============
      clf = cv2.face.LBPHFaceRecognizer_create()
      clf.train(faces,ids)
      clf.write("classifier.xml")
      cv2.destroyAllWindows()
      messagebox.showinfo("Result","Training datasets completed!!!")

         
                                                              


      

     
      
      








if __name__== "__main__":
   root=Tk()
   obj=Train(root)
   root.mainloop()