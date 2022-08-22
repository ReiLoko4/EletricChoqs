import PySimpleGUI as sg
import math as M

henry = 0
farad = 0
hz = 0
tensao = float(0)
amper = float(0)
result = float(0.0)

sg.theme("DarkBrown1")
result = float(0.0)

layout = [
    [
        sg.Radio(
            "",
            "Radio",
            True,
            enable_events=True,
            key="want",
            circle_color="grey",
            text_color="white",
        ),
        sg.Text("Impedância capacitiva", size=(16, 1), text_color="pink"),
        sg.Radio(
            "",
            "Radio",
            False,
            enable_events=True,
            key="want",
            circle_color="grey",
            text_color="white",
        ),
        sg.Text("Impedância indutiva", size=(16, 1), text_color="pink"),
    ],
    [sg.Text(size=(23, 1), key="out", text_color="white", background_color="orange")],
    [sg.Text("Digite o valor em µFarads", key="Rjr")],
    [sg.Input(size=(25, 5), key="input", text_color="yellow")],
    [
        sg.Text("Digite a frequência em Hz", key="Njr"),
        sg.Text("              "),
        sg.Text(
            "", size=(9, 1), key="out2", background_color="orange", text_color="white"
        ),
    ],
    [
        sg.Input(size=(25, 5), key="input2", text_color="yellow"),
        sg.Text("Volts"),
        sg.Input(size=(10, 5), key="input3", text_color="yellow"),
    ],
    [
        sg.Button(
            "Calcular", expand_x=True, bind_return_key=True, button_color="orange"
        ),
        sg.Button("Exit"),
    ],
]


def calcTens(result):
    tensao = values["input3"]
    if len(tensao) > 0:
        try:
            tensao = tensao.replace(",", ".")
            tensao = float(tensao)
            amper = round(tensao / result, 4)
            amper = str(amper)
            window["out2"].update("    " + amper + "A")
        except:
            print("erro")


def impCap():
    if len(values["input"]) and len(values["input2"]) > 0:
        try:
            farad = values["input"]
            hz = values["input2"]
            farad = farad.replace(",", ".")
            hz = hz.replace(",", ".")
            farad = float(farad)
            farad = farad / 1000000
            hz = float(hz)
            result = round(1 / (farad * hz * 2 * M.pi), 4)
            calcTens(result)
            result = str(result)
            window["out"].update("Resultado igual a " + result + "Ω")
        except:
            window["out"].update("Somente números")
    else:
        window["out"].update("Mal preenchido")


def impInd():
    if len(values["input"]) and len(values["input2"]) > 0:
        try:
            henry = values["input"]
            hz = values["input2"]
            henry = henry.replace(",", ".")
            hz = hz.replace(",", ".")
            henry = float(henry)
            hz = float(hz)
            result = round(henry * hz * 2 * M.pi, 4)
            calcTens(result)
            result = str(result)
            window["out"].update("Resultado igual a " + result + "Ω")
        except:
            window["out"].update("Somente números")
    else:
        window["out"].update("Mal preenchido")


window = sg.Window("Preguicios Calculator", layout)

while True:
    event, values = window.read()

    if values["want"]:
        window["Rjr"].update("Digite o valor em µFarads")
        window["Njr"].update("Digite a frequência em Hz")

    if not values["want"]:
        window["Rjr"].update("Digite o valor em Henrys")
        window["Njr"].update("Digite a frequência em Hz")

    if event == "Calcular":
        if values["want"] == True:
            try:
                impCap()
            except:
                window["out"].update("Erro")
        else:
            try:
                impInd()
            except:
                window["out"].update("Erro")

    if event in (None, "Exit"):
        break

window.close()
