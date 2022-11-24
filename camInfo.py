
from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import sqlite3
import uuid

from PIL import ImageTk, Image


def Cam(sg):
    print(sg)

    Reg = tk.Tk()
    
    Reg.title('!! CRIMINAL DETECTION AND RECOGNITION !!')
    Reg.geometry('1280x700')
    scrollbar = Scrollbar(Reg)
    scrollbar.pack(side = RIGHT, fill = Y )

    # Background Colors
    Reg.configure(background='black')

    
    Reg.resizable(width=False, height=False)

    
    Reg.iconbitmap('img/reglogo.ico')
    
   
    top_frame = Label(Reg, text='Cam Table Info Loader !!',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
   
    frame = LabelFrame(Reg, padx=400, pady=100, bg='white')
    frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    
  
   


    
    # Quit Button

    Quit = tk.Button(Reg, text = "Quit", width="10", command = Reg.destroy, bd = '3',  font = ('Times', 10, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.84)
