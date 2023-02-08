from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Chatbot:
    def __init__(self,root):
      self.root=root
      self.root.geometry("640x510+0+0")
      self.root.title("Chatbot")
      self.root.bind('<Return>',self.enter_func)

      main_frame=Frame(self.root,bd=4,bg="powder blue",width=540)
      main_frame.pack()

      img_chat=Image.open(r"Face attendance images\cbot.webp")
      img_chat=img_chat.resize((150,60),Image.ANTIALIAS)
      self.photoimg_chat=ImageTk.PhotoImage(img_chat)

      title_lbl=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=640,compound=LEFT,image=self.photoimg_chat,text="CHAT ME",font=("arial",30,"bold"),bg="white",fg="green")
      title_lbl.pack(side = TOP)

      self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
      self.text=Text(main_frame,width=65,height=19,bd=4,relief=RAISED,font=("arial",13),yscrollcommand=self.scroll_y.set)
      self.scroll_y.pack(side=RIGHT,fill=Y)
      self.text.pack()



      btm_frame=Frame(self.root,bd=4,bg='white',width=640)
      btm_frame.pack()

      label_1=Label(btm_frame,text="Type Something..",font=("arial",11,"bold"),bg="white",fg="green")
      label_1.grid(row=0,column=0,padx=5,sticky=W)

      self.entry=StringVar()
      self.entry1=ttk.Entry(btm_frame,textvariable=self.entry,width=37,font=("arial",13,"bold"))
      self.entry1.grid(row=0,column=1,padx=5,sticky=W)

      self.send=Button(btm_frame,text="Send>>",command=self.send,font=("arial",13,"bold"),width=8,bg='green')
      self.send.grid(row=0,column=2,padx=5,sticky=W)

      self.clear=Button(btm_frame,text="Clear Data",command=self.clear,font=("arial",10,"bold"),width=8,bg='red',fg='white')
      self.clear.grid(row=1,column=0,padx=5,sticky=W)

      self.msg=''
      self.label_2=Label(btm_frame,text=self.msg,font=("arial",11,"bold"),bg="white",fg="red")
      self.label_2.grid(row=1,column=1,padx=5,sticky=W)

    # ============== funcn declr ==================
    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')

    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if(self.entry.get()==''):
            self.msg='Please Enter Some Input'
            self.label_2.config(text=self.msg,fg='red')

        else:
            self.msg=''
            self.label_2.config(text=self.msg,fg='red')

        if(self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Bot: Hi')

        if(self.entry.get()=='hi'):
            self.text.insert(END,'\n\n'+'Bot: Hlw')

        elif(self.entry.get()=="how are you"):
            self.text.insert(END,'\n\n'+'Bot: Fine and you')

        elif(self.entry.get()=="fantastic"):
            self.text.insert(END,'\n\n'+'Bot: Nice to hear')

        elif(self.entry.get()=="who created you"):
            self.text.insert(END,'\n\n'+'Bot: Bhabatosh, using Python')

        elif(self.entry.get()=="what is your name"):
            self.text.insert(END,'\n\n'+'Bot: im Mr. Hacker')

        elif(self.entry.get()=="bye"):
            self.text.insert(END,'\n\n'+'Bot: Thank you for chatting')

        elif(self.entry.get()=="can you speak odia"):
            self.text.insert(END,'\n\n'+'Bot: I am still learnig it..')

        elif(self.entry.get()=="what is machine learning"):
            self.text.insert(END,'\n\n'+'Bot: the use and development of computer systems that are able to learn and adapt without following explicit instructions, by using algorithms and statistical models to analyse and draw inferences from patterns in data')

        elif(self.entry.get()=="how face recognition system work"):
            self.text.insert(END,'\n\n'+'Bot: It uses a digital camera to capture the image of the face, a computer for processing and analysis, and an output device for displaying the identification result')

        elif(self.entry.get()=="which algorith used in this project"):
            self.text.insert(END,'\n\n'+'Bot: harcascade fontal face,local binary pattern histogram algorith used in it')

        elif(self.entry.get()=="steps of face recognition system"):
            self.text.insert(END,'\n\n'+'Bot: Detection,Computer vision,Analysis,Recognition')

        elif(self.entry.get()=="who is ghumura"):
            self.text.insert(END,'\n\n'+'Bot: 20cse275,,Satyajeet Nath is known as ghumura..ha ha..and full name is Ghumura Para..')

        elif(self.entry.get()=="is Giet is good"):
            self.text.insert(END,'\n\n'+'Bot: No!! are you joking..')

        elif(self.entry.get()=="help"):
            self.text.insert(END,'\n\n'+'Bot: Pls tell which type of help you need')

        else:
            self.text.insert(END,'\n\n'+'Bot: Sorry I didnot get it..')

        






if __name__== "__main__":
   root=Tk()
   obj=Chatbot(root)
   root.mainloop()

    