
from functools import partial
from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import sqlite3 
from home import Home
from camInfo import Cam

import firebase_admin 
from firebase_admin import firestore
from firebase_admin import credentials



def Log():
    
    db = firestore.client()
  
    Login = tk.Tk()
    Login.geometry('1280x700')
    Login.title('!! CRIMINAL DETECTION AND RECOGNITION !!')


    Login.configure(background='black')

    
    Login.resizable(width=False, height=False)

  
    Login.iconbitmap('img/loginlogo.ico')

    
    top_frame = Label(Login, text='Login To System',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
   
    frame = LabelFrame(Login, padx=100, pady=100, bg='white')
    frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    
    
    def Search(arg = None):
        if username_entry.get() == '': 
            ms.showerror('Oops', 'Enter Username !!')
            
        elif password_entry.get() == '':
            ms.showerror('Oops', 'Enter Password !!')
            
        else:
            global username
            username = username_entry.get()
            global password
            password = password_entry.get()

          
            conn = sqlite3.connect('Database.db')

          
            with conn:
                cursor = conn.cursor()

            
            docs = list(db.collection('organizations').where('name','==',username).stream())

            for doc in docs :
                print(f'{doc.id} => {doc.to_dict()}')
            
           
            find_user = ('SELECT x FROM users WHERE Username = ? AND Password = ?')
            cursor.execute(find_user,(username, password))
            results = cursor.fetchall()
       
            if results:
                print(cursor)
                print(str(results[0][0])) # find_id successfully finally...!!! 

                Login.destroy()
                result = tk.Tk()
                result.geometry('1280x900')
                result.title('Thank You !')

            
                result.configure()

              
                result.resizable(width=False, height=False)

              

                frame = LabelFrame(result,text='Selection Option : ', padx=30, pady=30, bg='white', bd='5', relief='groove')
                frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)


              


                home = tk.Button(frame, text = "Cam details adder Page", width="35", bd = '3', command=partial(
    Home, str(results[0][0]),docs[0].id), font = ('Times', 20, 'bold'), bg='#7268A6',relief='groove', justify = 'center', pady='5')
                home.pack(pady=100)

                table = tk.Button(frame, text = "Cam details Page", width="35", bd = '3', command=partial(
    Cam, str(results[0][0])), font = ('Times', 20, 'bold'), bg='#7268A6',relief='groove', justify = 'center', pady='5')
                table.pack(pady=100)
               





              
                
                Txt = Text(result, height=10, width=120)
                Txt.pack()
                Txt.insert(END, 'Heyy Mr/Mrs. '+ username +'\nThank You For Using Our CDR System !!!!')
           

           
            else:
                ms.showerror('Oops','User Not Found !! Check Username and Password Again !!')


    username = tk.Label(frame, text = 'Username',font=('Arial',15, 'bold'),bg='white', fg='green')
    password = tk.Label(frame, text = 'Password', font = ('Arial',15,'bold'),bg='white', fg='green')   

   
    username_entry = tk.Entry(frame, font=('calibre',15,'normal'), justify = 'center', bg='#FBB13C')
    username_entry.bind('<Return>', Search)
    password_entry=tk.Entry(frame, font = ('calibre',15,'normal'), show = '*', justify = 'center', bg='#FBB13C') 
    password_entry.bind('<Return>', Search)
    
 
    submit=tk.Button(frame,text = 'Login', command = Search, width="15",bd = '3',  font = ('Times', 15, 'bold'), bg='#581845', fg='white',relief='groove', justify = 'center', pady='5') 
  
    username.pack()
    username_entry.focus_set()
    username_entry.pack()
    
    
    label = Label(frame, bg='white').pack()
    
    password.pack() 
    password_entry.pack()


    label = Label(frame, bg='white').pack()
    
    submit.pack()
    

    

    
    # Quit Button

    Quit = tk.Button(Login, text = "Quit", width="10", command = Login.destroy, bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.775)
