
from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import sqlite3
import uuid

from PIL import ImageTk, Image

import firebase_admin 
from firebase_admin import firestore
from firebase_admin import credentials


def Register():

    db = firestore.client()
    
  
    Reg = tk.Tk()
    
    Reg.title('!! CRIMINAL DETECTION AND RECOGNITION !!')
    Reg.geometry('1280x700')
    scrollbar = Scrollbar(Reg)
    scrollbar.pack(side = RIGHT, fill = Y )

    
    Reg.configure(background='black')

 
    Reg.resizable(width=False, height=False)

  
    Reg.iconbitmap('img/reglogo.ico')
    
   
    top_frame = Label(Reg, text='Registration',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
   
    frame = LabelFrame(Reg, padx=400, pady=100, bg='white')
    frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    
    
    def database(arg=None):

      
        name = name_entry.get()
        email = email_entry.get()

   
        mobile = mobile_entry.get()
        try:
            mobile = int(mobile)
        except:
            ms.showerror('Oops', 'Please Enter a Valid Phone Number !!!')

        username = username_entry.get()
        password = password_entry.get()
        confirm = confirm_entry.get()
        mob1 = mob1_entry.get()
        mob2 = mob2_entry.get()

      
        validation = []

  
        y=uuid.uuid4()
        x=str(y)
        validation.append(name)
        validation.append(email)
        validation.append(mobile)
        validation.append(username)
        validation.append(password)
        validation.append(confirm)
        validation.append(mob1)
        validation.append(mob2)
        validation.append(x)
       

        condition = True
        
     
        for ele in validation:
            if ele == '':
                
                condition = False
                break

        if condition:
            
           
            if password != confirm:
                ms.showerror('Oops', 'Password Does Not Match!!!')    
                
            else:
               
                conn = sqlite3.connect('Database.db')

              
                with conn:
                    cursor = conn.cursor()

              
                cursor.execute('CREATE TABLE IF NOT EXISTS Users (FullName TEXT NOT NULL, Email TEXT NOT NULL, Mobile TEXT NOT NULL, Username TEXT NOT NULL, Password TEXT NOT NULL, Mob1 TEXT NOT NULL, Mob2 TEXT NOT NULL,x TEXT NOT NULL)')

               
                cursor.execute('INSERT INTO Users (FullName, Email, Mobile, Username, Password, Mob1, Mob2 ,x) VALUES (?,?,?,?,?,?,?,?)', (name, email, mobile, username, password, mob1, mob2, x))
                conn.commit()


                org_ref = db.collection('organizations').document(name)

                org_ref.set({
                    'name': name,
                    'email': email,
                    'password':password,
                    'username': username,
                    'mobile 1': mob1,
                    'mobile 2': mob2,
                })

               
                ms.showinfo('Great !! ', 'Account Created Successfully!! Now You Can Login To System!!')

               
                Reg.destroy()
            
        else:
            ms.showerror('Oops', 'Please Fill All The Input Fields')
    
   
    name = tk.Label(frame, text = 'Full Name', font=('Arial',10, 'bold'), bg='white', fg='green')
    email = tk.Label(frame, text = 'Email', font=('Arial',10, 'bold'), bg='white', fg='green')
    mobile = tk.Label(frame, text = 'Mobile No.', font=('Arial',10, 'bold'), bg='white', fg='green')
    username = tk.Label(frame, text = 'Username', font=('Arial',10, 'bold'), bg='white', fg='green')                    
    password = tk.Label(frame, text = 'Password', font = ('Arial',10,'bold'), bg='white', fg='green')
    confirm = tk.Label(frame, text = 'Confirm Password', font=('Arial',10, 'bold'), bg='white', fg='green')
    mob1 = tk.Label(frame, text = 'mob1', font = ('Arial',10,'bold'), bg='white', fg='green')
    mob2 = tk.Label(frame, text = 'mob2', font=('Arial',10, 'bold'), bg='white', fg='green')
  
    

    
    name_entry = tk.Entry(frame ,font=('Arial',10,'normal'), bg='#FBB13C')
    name_entry.bind("<Return>", database)
    email_entry = tk.Entry(frame,font=('Arial',10,'normal'), bg='#FBB13C')
    email_entry.bind("<Return>",database)
    mobile_entry = tk.Entry(frame,font=('Arial',10,'normal'), bg='#FBB13C')
    mobile_entry.bind("<Return>",database)
    username_entry = tk.Entry(frame,font=('Arial',10,'normal'), bg='#FBB13C')
    username_entry.bind("<Return>",database)
    password_entry=tk.Entry(frame, font = ('Arial',10,'normal'), show = '*', bg='#FBB13C')
    password_entry.bind("<Return>",database)
    confirm_entry=tk.Entry(frame, font = ('Arial',10,'normal'), show = '*', bg='#FBB13C')
    confirm_entry.bind("<Return>",database)
    mob1_entry=tk.Entry(frame, font = ('Arial',10,'normal'),bg='#FBB13C')
    mob1_entry.bind("<Return>",database)
    mob2_entry=tk.Entry(frame, font = ('Arial',10,'normal'),bg='#FBB13C')
    mob2_entry.bind("<Return>",database)
   

       
    
    submit=tk.Button(frame,text = 'Register', command = database, width="10",bd = '3',  font = ('Times', 10, 'bold'),bg='#581845', fg='white',relief='groove', justify = 'center', pady='5'  ) 
       
    
    name.pack()
    name_entry.focus_set()
    name_entry.pack()
    
    
    label = Label(frame, bg='white').pack()
    
    email.pack()
    email_entry.pack()

    
    label = Label(frame, bg='white').pack()
    
    mobile.pack()
    mobile_entry.pack()

    
    label = Label(frame, bg='white').pack()
    
    username.pack() 
    username_entry.pack()

    
    label = Label(frame, bg='white').pack()
    
    password.pack() 
    password_entry.pack()

    
    label = Label(frame, bg='white').pack()
    
    confirm.pack()
    confirm_entry.pack()

   

    
    label = Label(frame, bg='white').pack()

    mob1.pack()
    mob1_entry.pack()

   

    
    label = Label(frame, bg='white').pack()

    mob2.pack()
    mob2_entry.pack()

   

 
    label = Label(frame, bg='white').pack()
    
    submit.pack()

    

    Quit = tk.Button(Reg, text = "Quit", width="10", command = Reg.destroy, bd = '3',  font = ('Times', 10, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.84)
