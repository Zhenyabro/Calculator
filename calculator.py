import PySimpleGUI as sg

# Установите тему
sg.theme('DarkGrey9')

layout = [
    [sg.Input(size=(20, 4), key="expression")],
    [sg.Button("7"), sg.Button("8"), sg.Button("9"), sg.Button("/")],
    [sg.Button("4"), sg.Button("5"), sg.Button("6"), sg.Button("*")],
    [sg.Button("1"), sg.Button("2"), sg.Button("3"), sg.Button("-")],
    [sg.Button("0"), sg.Button("."), sg.Button("="), sg.Button("+")],
    [sg.Button("Clear"), sg.Button("Leave")]
]

window = sg.Window('Calculator', layout, icon='icon.ico')

result = ""

while True:
    event, value = window.read()
    if event == sg.WINDOW_CLOSED or event == "Leave":
        break
    elif event == "Clear":
        result = ""
        window["expression"].update(result)
    elif event == "=":
        try:
            result = str(eval(result))
            window["expression"].update(result)
        except:
            window["expression"].update("Error!")
    else:
        result += event
        window["expression"].update(result)

window.close()
