import PySimpleGUI as sg

sg.theme('DarkAmber')  # Keep things interesting for your users

layout = [[sg.Input(key='-IN1-', size=6)],
          [sg.Button('', key='-0-', size=[3, 1], button_color='white'),
           sg.Button('', key='-1-', size=[3, 1], button_color='white'),
           sg.Button('', key='-2-', size=[3, 1], button_color='white'),
           sg.Button('', key='-3-', size=[3, 1], button_color='white'),
           sg.Button('', key='-4-', size=[3, 1], button_color='white')],
          [sg.Text('Resultado', key='OUTlen'), sg.Text(key='-OUT0-'), sg.Text(key='-OUT1-'), sg.Button('Mais')],
          [sg.Button('Filtrar'), sg.Button('Limpar'), sg.Button('Reset'), sg.Exit()]]

window = sg.Window('Wheeldle Breaker', layout)


def remover_pretas(letra):
    posicoes = []
    if not (letra in verdes):
        if not (letra in pretas):
            pretas.insert(0, letra)
            print('removendo', letra, ' das pretas len= ', len(leitura))
            for x in range(len(leitura)):
                for i in range(0, 5):
                    if leitura[x][i] == letra:
                        posicoes.insert(0, x)
                        break

            for x in range(len(posicoes)):
                remover = posicoes[x]
                leitura.pop(remover)


def salvar_verde(pos, letra):
    posicoes = []
    print('removendo', letra, ' das verdes len= ', len(leitura))
    for x in range(len(leitura)):
        if leitura[x][pos] != letra:
            posicoes.insert(0, x)

    for x in range(len(posicoes)):
        remover = posicoes[x]
        leitura.pop(remover)


def salvar_amarela(pos, letra):
    posicoes = []
    for x in range(len(leitura)):
        contem = 0
        for i in range(0, 5):
            if leitura[x][i] == letra:
                contem = contem + 1
        if contem == 0:
            posicoes.insert(0, x)

    for x in range(len(posicoes)):
        remover = posicoes[x]
        leitura.pop(remover)

    posicoes = []
    for x in range(len(leitura)):
        if leitura[x][pos] == letra:
            posicoes.insert(0, x)

    for x in range(len(posicoes)):
        remover = posicoes[x]
        leitura.pop(remover)


def rotatecolor(pos):
    if cores[pos] == 'yellow':
        cores[pos] = 'black'
    elif cores[pos] == 'black':
        cores[pos] = 'green'
    else:
        cores[pos] = 'yellow'


def janelamais():
    layout = [[sg.Text("Mais palavras")],
              [sg.Text(leitura[0]), sg.Text(leitura[1]), sg.Text(leitura[2])],
              [sg.Text(leitura[3]), sg.Text(leitura[4]), sg.Text(leitura[5])]]

    window = sg.Window("Second Window", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        window.close()


with open("sgb-words.txt", "r") as arquivo:
    leitura = arquivo.read().split()

radios1 = []
radios2 = []
radios3 = []
radios4 = []
radios5 = []
verdes = []
pretas = []

cores = ['white', 'white', 'white', 'white', 'white']

while True:  # The Event Loop
    event, values = window.read()
    # print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Filtrar':
        for i in range(0, 4):
            if cores[i] == 'yellow':
                salvar_amarela(i, values['-IN1-'][i])
            elif cores[i] == 'black':
                remover_pretas(values['-IN1-'][i])
            elif cores[i] == 'green':
                salvar_verde(i, values['-IN1-'][i])
        window['OUTlen'].update(len(leitura))
        window['-OUT0-'].update(leitura[0])
        if len(leitura) > 1:
            window['-OUT1-'].update(leitura[1])

    if event == 'Limpar':
        window['-IN1-'].update('')

    if event == 'Reset':
        with open("sgb-words.txt", "r") as arquivo:
            leitura = arquivo.read().split()
        window['OUTlen'].update(len(leitura))
        window['-OUT0-'].update(leitura[0])
        if len(leitura) > 1:
            window['-OUT1-'].update(leitura[1])

    if event == '-0-':
        rotatecolor(0)
        window['-0-'].update(button_color=cores[0])
    if event == '-1-':
        rotatecolor(1)
        window['-1-'].update(button_color=cores[1])
    if event == '-2-':
        rotatecolor(2)
        window['-2-'].update(button_color=cores[2])
    if event == '-3-':
        rotatecolor(3)
        window['-3-'].update(button_color=cores[3])
    if event == '-4-':
        rotatecolor(4)
        window['-4-'].update(button_color=cores[4])

    if event == 'Mais':
        janelamais()

    print(len(leitura), leitura[0])

window.close()
