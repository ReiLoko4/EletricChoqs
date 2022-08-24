import PySimpleGUI as sg


result = 0

sg.theme("DarkTanBlue")


layout = [
    [
        sg.Text("Padrão"),
        sg.Radio("", "r1", True, enable_events=True, key="p1"),
        sg.Text("mili"),
        sg.Radio("", "r1", False, enable_events=True, key="m1"),
        sg.Text("Micro"),
        sg.Radio("", "r1", False, enable_events=True, key="µ1"),
    ],
    [
        sg.Input(size=(25, 5), key="input"),
        sg.Text(
            "Padrão",
            size=(5, 1),
            key="slct",
            text_color="Yellow",
            background_color="Blue",
        ),
    ],
    [
        sg.Text("Padrão"),
        sg.Radio("", "r2", True, enable_events=True, key="p2"),
        sg.Text("mili"),
        sg.Radio("", "r2", False, enable_events=True, key="m2"),
        sg.Text("Micro"),
        sg.Radio("", "r2", False, enable_events=True, key="µ2"),
    ],
    [
        sg.Text(
            "      ",
            size=(22, 1),
            key="out",
            text_color="Yellow",
            background_color="Grey",
        ),
        sg.Text(
            "Padrão",
            size=(5, 1),
            key="slct2",
            text_color="Yellow",
            background_color="Blue",
        ),
    ],
    [
        sg.Button(
            "Converter", expand_x=True, button_color="Black", bind_return_key=True
        ),
        sg.Button("Exit"),
    ],
]

window = sg.Window("Automatic converter", layout)

while True:
    event, values = window.read()

    if values["p1"]:
        window["slct"].update("Padrão")
    if values["m1"]:
        window["slct"].update("m")
    if values["µ1"]:
        window["slct"].update("µ")

    if values["p2"]:
        window["slct2"].update("Padrão")
    if values["m2"]:
        window["slct2"].update("m")
    if values["µ2"]:
        window["slct2"].update("µ")

    if event == "Converter":
        if values["p1"]:

            if values["p2"]:
                window["out"].update(values["input"])

            if values["m2"]:
                try:
                    result = values["input"]
                    result = result.replace(",", ".")
                    result = float(result)
                    result = round(result * 1000, 4)
                    result = str(result)
                    window["out"].update(result + " m")
                except:
                    window["out"].update("")

            if values["µ2"]:
                try:
                    result = values["input"]
                    result = result.replace(",", ".")
                    result = float(result)
                    result = round(result * 1000000, 4)
                    result = str(result)
                    window["out"].update(result + " µ")
                except:
                    window["out"].update("")

        if values["m1"]:

            if values["p2"]:
                try:
                    result = values["input"]
                    result = result.replace(",", ".")
                    result = float(result)
                    result = round(result / 1000, 4)
                    result = str(result)
                    window["out"].update(result)
                except:
                    window["out"].update("")

            if values["m2"]:
                window["out"].update(values["input"] + " m")

            if values["µ2"]:
                try:
                    result = values["input"]
                    result = result.replace(",", ".")
                    result = float(result)
                    result = round(result * 1000, 4)
                    result = str(result)
                    window["out"].update(result + " µ")
                except:
                    window["out"].update("")

        if values["µ1"]:

            if values["p2"]:
                try:
                    result = values["input"]
                    result = result.replace(",", ".")
                    result = float(result)
                    result = result / 1000000
                    result = str(result)
                    window["out"].update(result)
                except:
                    window["out"].update("")

            if values["m2"]:
                try:
                    result = values["input"]
                    result = result.replace(",", ".")
                    result = float(result)
                    result = round(result / 1000, 4)
                    result = str(result)
                    window["out"].update(result + " m")
                except:
                    window["out"].update("")

            if values["µ2"]:
                window["out"].update(values["input"] + " µ")

    if event in (None, "Exit"):
        break


window.close()
