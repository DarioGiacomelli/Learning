#!/usr/bin/env python
import PySimpleGUI as sg

"""
    Simple test harness to demonstate how to use the CalendarButton and the get date popup
"""
# sg.theme('Dark Red')
layout = [[sg.Text('Date Chooser Test Harness', key='-TXT-')],
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