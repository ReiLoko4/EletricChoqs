import PySimpleGUI as sg

result = float(0)
language = [
    "First number:",
    "Second number:",
    "The result is: ",
    "Only numbers!",
    "Please type bro!",
    "The formula is (A . B) / (A + B)",
    "Made for capacitors, inductors and resistors.",
    "Made in Python with the PySimpleGUI library.",
    "Version ",
    "Calculate",
    "Exit"
]

sg.theme("DarkBlue")


layout = [
    [
        sg.Text(
            "", key="out", background_color="white", text_color="black", size=(30, 1)
        ),
        sg.ButtonMenu(
            "Language",
            [["Eng", "BR"], ["English", "PT-BR"]],
            key="slct",
            border_width=2,
        ),
    ],
    [sg.Text(language[0], text_color="yellow", key="txt1", size=(20, 1))],
    [sg.Input(key="In-1")],
    [sg.Text(language[1], text_color="yellow", key="txt2", size=(20, 1))],
    [sg.Input(key="In-2")],
    [
        sg.Button("Calculate", expand_x=True, bind_return_key=True, key="Return"),
        sg.Button("?", size=(2, 1)),
        sg.Button("Exit", key="Exit"),
    ],
]


def update():
    window["out"].update("")
    window["txt1"].update(language[0])
    window["txt2"].update(language[1])
    window["Return"].update(language[9])
    window["Exit"].update(language[10])


def Associ():
    if len(values["In-1"]) and len(values["In-2"]) > 0:
        try:
            RLC1 = values["In-1"]
            RLC2 = values["In-2"]
            RLC1 = RLC1.replace(",", ".")
            RLC2 = RLC2.replace(",", ".")
            RLC1 = float(RLC1)
            RLC2 = float(RLC2)
            result = round((RLC1 * RLC2) / (RLC1 + RLC2), 4)
            result = str(result)
            window["out"].update(language[2] + result)
        except:
            window["out"].update(language[3])
    else:
        window["out"].update(language[4])


window = sg.Window("Eletric Association", layout)

while True:
    event, values = window.read()

    if event in (None, "Exit"):
        break

    if event == "Calculate":
        window["Eletric Association"].update("pobre")
        Associ()

    if event == "slct":
        if values["slct"] == "English":
            language = [
                "First number:",
                "Second number:",
                "The result is: ",
                "Only numbers!",
                "Please type bro!",
                "The formula is (A . B) / (A + B)",
                "Made for capacitors, inductors and resistors.",
                "Made in Python with the PySimpleGUI library.",
                "Version ",
                "Calculate",
                "Exit"
            ]
            update()
        else:
            language = [
                "Primeiro número:",
                "Segundo número:",
                "O resultado é: ",
                "Apenas números!",
                "Por favor digite meu cria!",
                "A fórmula é (A . B) / (A + B)",
                "Feito para capacitores, indutores e resistores.",
                "Feito em Python com a biblioteca PySimpleGUI.",
                "Versão ",
                "Calcular",
                "Sair"
            ]
            update()
    if event == "?":
        window.disappear()
        sg.popup(
            language[5],
            language[6],
            language[7],
            language[8] + sg.version,
            grab_anywhere=True,
        )
        window.reappear()


window.close()
