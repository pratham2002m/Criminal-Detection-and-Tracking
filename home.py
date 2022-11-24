
from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import sqlite3
import uuid

import firebase_admin 
from firebase_admin import firestore
from firebase_admin import credentials

from PIL import ImageTk, Image


def Home(owner,id):
    
    print(owner)
    print(id)

    Reg = tk.Tk()
    
    Reg.title('!! CRIMINAL DETECTION AND RECOGNITION !!')
    Reg.geometry('1280x700')
    scrollbar = Scrollbar(Reg)
    scrollbar.pack(side = RIGHT, fill = Y )

    
    Reg.configure(background='black')

    
    Reg.resizable(width=False, height=False)

  
    Reg.iconbitmap('img/reglogo.ico')
    
  
    top_frame = Label(Reg, text='Add data of cameras !!',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
 
    frame = LabelFrame(Reg, padx=400, pady=100, bg='white')
    frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
  
    def database(arg=None):
      
        db = firestore.client()

        ow=owner
        location = location_entry.get()
        incharge_name = incharge_name_entry.get()

       
        incharge_mobile = incharge_mobile_entry.get()
        try:
           incharge_mobile = int(incharge_mobile)
        except:
            ms.showerror('Oops', 'Please Enter a Valid Phone Number !!!')

        lattitude = lattitude_entry.get()
        longitude = longitude_entry.get()
       

        
        validation = []

       
        y=uuid.uuid4()
        x=str(y)
        validation.append(location)
        validation.append(incharge_name)
        validation.append(incharge_mobile)
        validation.append(lattitude)
        validation.append(longitude)
        validation.append(x)
        validation.append(ow)
       

     
        condition = True
        
        
        for ele in validation:
            if ele == '':
                condition = False
                break

        if condition:
          
         
                conn = sqlite3.connect('Database.db')

               
                with conn:
                    cursor = conn.cursor()

               
                cursor.execute('CREATE TABLE IF NOT EXISTS Camm (ow TEXT NOT NULL, x TEXT NOT NULL, Location TEXT NOT NULL, Lattitude TEXT NOT NULL, Longitude TEXT NOT NULL, Incharge_name TEXT NOT NULL, Incharge_mobile TEXT NOT NULL)')

             
                cursor.execute('INSERT INTO Camm (ow, x, Location, Lattitude, Longitude, Incharge_name, Incharge_mobile) VALUES (?,?,?,?,?,?,?)', (ow, x, location, lattitude, longitude, incharge_name, incharge_mobile))
                conn.commit()

                cam_add = db.collection('organizations').document(id).collection('cameras')
                cam_add.add({
                    'location' : location,
                    'lattitude' : lattitude,
                    'longitude': longitude,
                    'incharge': incharge_name,
                    'incharge_mobile' : incharge_mobile
                })

              
                ms.showinfo('Great !! ', 'Camera data added successfully....!!')

                Home(ow)
            
        else:
            ms.showerror('Oops', 'Please Fill All The Input Fields...')
    
    
    location = tk.Label(frame, text = 'location', font=('Arial',10, 'bold'), bg='white', fg='green')
    lattitude = tk.Label(frame, text = 'lattitude', font=('Arial',10, 'bold'), bg='white', fg='green')
    longitude = tk.Label(frame, text = 'longitude', font=('Arial',10, 'bold'), bg='white', fg='green')
    incharge_name = tk.Label(frame, text = 'Incharge Name', font=('Arial',10, 'bold'), bg='white', fg='green')
    incharge_mobile = tk.Label(frame, text = 'Incharge Mobile Number', font=('Arial',10, 'bold'), bg='white', fg='green')                    
    
  
    

   

    location_entry = tk.Entry(frame ,font=('Arial',10,'normal'), bg='#FBB13C')
    location_entry.bind("<Return>", database)

    lattitude_entry = tk.Entry(frame ,font=('Arial',10,'normal'), bg='#FBB13C')
    lattitude_entry.bind("<Return>", database)

    longitude_entry = tk.Entry(frame,font=('Arial',10,'normal'), bg='#FBB13C')
    longitude_entry.bind("<Return>",database)

    incharge_name_entry = tk.Entry(frame,font=('Arial',10,'normal'), bg='#FBB13C')
    incharge_name_entry.bind("<Return>",database)

    incharge_mobile_entry = tk.Entry(frame,font=('Arial',10,'normal'), bg='#FBB13C')
    incharge_mobile_entry.bind("<Return>",database)
    
   

       


    submit=tk.Button(frame,text = 'Add cam infos!', command = database, width="30",bd = '3',  font = ('Times', 30, 'bold'),bg='#581845', fg='white',relief='groove', justify = 'center', pady='5'  ) 

    location.pack()
    location_entry.focus_set()
    location_entry.pack()

    label = Label(frame, bg='white').pack()
    
    lattitude.pack()
    lattitude_entry.pack()
    
    
    label = Label(frame, bg='white').pack()
    
    longitude.pack()
    longitude_entry.pack()

  
    label = Label(frame, bg='white').pack()
    
    incharge_name.pack()
    incharge_name_entry.pack()

   
    label = Label(frame, bg='white').pack()
    
    incharge_mobile.pack() 
    incharge_mobile_entry.pack()


   
    label = Label(frame, bg='white').pack()
    
    submit.pack()


    Quit = tk.Button(Reg, text = "Quit", width="10", command = Reg.destroy, bd = '3',  font = ('Times', 10, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.84)
