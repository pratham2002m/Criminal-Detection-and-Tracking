import PySimpleGUI as sg

def new_layout(i):
    return [
            [sg.T("    ")],
            [sg.T("cam Id:         "), sg.InputText(key=("-q-", i))], 
            [sg.T("Lattitude:      "), sg.InputText(key=("-q-", i))],
            [sg.T("Longitude:      "), sg.InputText(key=("-q-", i))],
            [sg.T("location:       "), sg.InputText(key=("-q-", 1))],
            [sg.T("police guard no:"), sg.InputText(key=("-q-", i))], 
    ]



category_list = ("Police Incharge","Other")

column_layout = [
    [sg.T("    ")],
    [sg.T("Cam Id:            "), sg.InputText(key=("-q-", 1))], 
    [sg.T("Lattitude:          "), sg.InputText(key=("-q-", 1))],
    [sg.T("Longitude:        "), sg.InputText(key=("-q-", 1))],
    [sg.T("location:           "), sg.InputText(key=("-q-", 1))],
    [sg.T("police guard no:"), sg.InputText(key=("-q-", 1))], 
    
]

layout = [
    [sg.T("    ")],
    [sg.T("Organisation: "), sg.InputText(size=(80,1), key="-t-")],
    [sg.T("    ")],
    [sg.T("Address      : "), sg.InputText(size=(80,1), key="-t-")],
    [sg.T("    ")],
    [sg.T("Category     : "), sg.Combo(values=category_list, size=(15, len(category_list)), default_value="Police Incharge", key="-cat-", enable_events=True),sg.T("Phone number: "), sg.InputText(size=(30,1), key="-t-")],
    [sg.T("    ")],
    [sg.Column(column_layout,key="-Column-",vertical_scroll_only=True)],
    [sg.T("    ")],
    [sg.Submit(button_text="Update/Insert"), sg.Cancel(button_text="Cancel"),sg.Button(button_text="Add another field: ",enable_events=True, image_data="", key="-plus-")],
]

window = sg.Window('Criminal Detection and Recognition !', layout,finalize=True,resizable=True)
window.maximize()

i = 1
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit', 'Cancel'):
        break
    elif event == '-plus-':
        if i<3:
            window.extend_layout(window['-Column-'], new_layout(i))

            i += 1
    print(event, values)

event, values = window.read()
window.close()