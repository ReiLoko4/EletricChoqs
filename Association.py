import PySimpleGUI as sg

result = 0

sg.theme("DarkBlue")

layout = [[sg.Text("Resistor or Capacitor"), sg.Radio("", "r1", True, enable_events = True, key="Mode1"),
sg.Text("Inductor"), sg.Radio("", "r1", False, enable_events = True, key="Mode2")
],
[sg.Text("Resistor or Capacitor 1:", text_color="yellow", key="txt2", size=(20,1))],
[sg.Input(key = "In-1")],
[sg.Text("Resistor or Capacitor 2:", text_color="yellow", key="txt1", size=(20,1))],
[sg.Input(key = "In-2")],
[sg.Button("Calculate", expand_x=True), sg.Button("?"), sg.Button("Exit")]
]



window = sg.Window("Eletric Association", layout)

while True:
    event, values = window.read()
    print(event, values)

    if event in (None, "Exit"):
        break

    if event == "Mode1":
        window["txt1"].update("Resistor or Capacitor 1:")
        window["txt2"].update("Resistor or Capacitor 2:")

    if event == "Mode2":
        window["txt1"].update("Inductor 1:")
        window["txt2"].update("Inductor 2:")



window.close()