import PySimpleGUI as sg

result = float(0)

sg.theme("DarkBlue")

layout = [[sg.Text("", key="out", background_color="white",text_color="black", size = (20,1))],
[sg.Text("First number:", text_color="yellow", key="txt1", size=(20,1))],
[sg.Input(key = "In-1")],
[sg.Text("Second number:", text_color="yellow", key="txt2", size=(20,1))],
[sg.Input(key = "In-2")],
[sg.Button("Calculate", expand_x=True, bind_return_key=True), sg.Button("?", size=(2,1)), sg.Button("Exit")]
]

layout2 =[[sg.Text("Formula is:")],[sg.Button("Exit")]]

def Associ():
    if len(values["In-1"]) and len(values["In-2"]) > 0:
        try:
            ric1 = values["In-1"]
            ric2 = values["In-2"]
            ric1 = ric1.replace(",", ".")
            ric2 = ric2.replace(",", ".")
            ric1 = float(ric1)
            ric2 = float(ric2)
            result = round((ric1 * ric2)/(ric1 + ric2), 4)
            result = str(result)
            window["out"].update("Result is " + result)
        except:
            window["out"].update("Only numbers!")
    else:
        window["out"].update("Please type bro!")


window = sg.Window("Eletric Association", layout)

while True:
    event, values = window.read()
    print(event, values)

    if event in (None, "Exit"):
        break

    if event == "Calculate":
   
        Associ()

    
window.close() 