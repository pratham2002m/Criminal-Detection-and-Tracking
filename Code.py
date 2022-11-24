
from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import sqlite3
from login import Log
from register import Register
from PIL import ImageTk, Image


import firebase_admin 
from firebase_admin import firestore
from firebase_admin import credentials




cred = credentials.Certificate("criminal-detection-n-tracking-firebase-adminsdk-q3hv6-0a9f4f38d2.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

system = tk.Tk()


system.geometry('1280x900')


system.configure(background='black')


system.resizable(width=False, height=False)


system.title('Login and Registration System')

system.iconbitmap('img/Logo.ico')

system.wm_title('!! CRIMINAL DETECTION AND RECOGNITION !!')


top_frame = Label(system, text='!! CRIMINAL DETECTION AND RECOGNISATION !!',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
top_frame.pack(side='top')



canvas = Canvas(system, width=500, height=350)


frame = LabelFrame(system,text='Selection Option : ', padx=70, pady=70, bg='white', bd='5', relief='groove')
frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)



login = tk.Button(frame, text = "Login", width="30", bd = '3', command = Log, font = ('Times', 12, 'bold'), bg='#7268A6',relief='groove', justify = 'center', pady='5')
login.pack()


label = Label(frame, bg='white').pack()
  
register = tk.Button(frame, text = "Register", width="30", bd = '3',  command = Register, font = ('Times', 12, 'bold'), bg='#2A1F2D',fg='white', relief='groove', justify = 'center', pady='5')
register.pack()



def Quit():
    response = ms.askokcancel('Exit!', 'Do you really want to exit ??')
    if response == 1:
        system.destroy()
    else:
        pass
    
Quit = tk.Button(system, text = "Quit", width="10", command = Quit, bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
Quit.place(anchor ='sw',rely=1,relx=0.775)

system.mainloop()
    
