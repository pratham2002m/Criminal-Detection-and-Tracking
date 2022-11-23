import PySimpleGUI as sg

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("criminal-detection-n-tracking-firebase-adminsdk-q3hv6-0a9f4f38d2.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://criminal-detection-n-tracking-default-rtdb.firebaseio.com'
    })

ref = db.reference('organizations/')


def new_layout(i):
    return [
            [sg.T("    ")],
            [sg.T("cam Id:         "), sg.InputText(key=("-q-", i))], 
            [sg.T("Lattitude:      "), sg.InputText(key=("-q-", i))],
            [sg.T("Longitude:      "), sg.InputText(key=("-q-", i))],
            [sg.T("location:       "), sg.InputText(key=("-q-", i))],
            [sg.T("police guard no:"), sg.InputText(key=("-q-", i))], 
    ]



category_list = ("Police Incharge","Other")

column_layout = [
    [sg.T("    ")],
    [sg.T("Cam Id:            "), sg.InputText(key='-CAMID-',do_not_clear=False)], 
    [sg.T("Lattitude:          "), sg.InputText(key='-Lattitude-',do_not_clear=False)],
    [sg.T("Longitude:        "), sg.InputText(key='-Longitude-',do_not_clear=False)],
    [sg.T("Location:           "), sg.InputText(key='-Location-',do_not_clear=False)],
    # [sg.T("police guard no:"), sg.InputText(key='',do_not_clear=False)], 
    
]

layout = [
    [sg.T("    ")],
    [sg.T("Organisation Name: "), sg.InputText(size=(80,1),key='-Organisation Name-')],
    [sg.T("    ")],
    [sg.T("Address      : "), sg.InputText(size=(80,1),key='-Address-')],
    [sg.T("    ")],
    [sg.T("Category     : "), sg.Combo(values=category_list, size=(15, len(category_list)), default_value="Police Incharge", key="-Category-", enable_events=True),sg.T("Phone number: "), sg.InputText(size=(30,1),key='-Mobile No-')],
    [sg.T("    ")],
    [sg.Column(column_layout,key="-Column-",vertical_scroll_only=True)],
    [sg.T("    ")],
    [sg.Button('Submit'), sg.Cancel("Cancel"),sg.Button('Add Camera')],
]

window = sg.Window('Criminal Detection and Recognition !', layout,finalize=True,resizable=True)
window.maximize()

camera_coord = []

i = 1
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit', 'Cancel'):
        break
    elif event == 'Add Camera':

        event, values = window.read()
        print("Submit wevent treiggered",values)
        print("Submit wevent treiggered",values['-Organisation Name-'])
        org_ref = ref.child(values['-Organisation Name-'])
        cam_ref = org_ref.child('cameras/')



        cam_ref.update({
            f'cam{i}': {
                'id': str(values['-CAMID-']),
                'lattitude': str(values['-Lattitude-']),
                'longitude': str(values['-Longitude-']),
                'location':  str(values['-Location-']),
            }
        })

        i+=1
        

    elif event == 'Submit' :
        org_ref.update({
            'Organization Name':str(values['-Organisation Name-']),
            'Address':str(values['-Address-']),
            'Category':str(values['-Category-']),
            'Mobile No': str(values['-Mobile No-'])
        })
    elif event == 'Cancel' :

        break

 
    print(event, values)

event, values = window.read()
window.close()