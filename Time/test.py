import PySimpleGUI as sg

layout = [[sg.Text('Tijdsregistratie', key='-TXT-')],
      [sg.Text(key='-IN-', size=(20,1))],
      [sg.CalendarButton('Datum',  target='-IN-', locale='nl_NL', begin_at_sunday_plus=1, format='%d/%m/%Y' )]]

window = sg.Window('window', layout).finalize()
window.Maximize()

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

window.close()