from PySimpleGUI import PySimpleGUI as sg
fnt = 'Arial 12'
sg.theme('BlueMono')
layout = [
    [sg.Image(r'C:\Users\aguil\OneDrive\Área de Trabalho\VERSAO1_PROJETOSI\logo.png')],
    [sg.Text('Vendedor'),sg.Input(key='vendedor', size=(20,1))],
    [sg.Text('Produto'),sg.Input(key='produto')],
    [sg.Text('Valor_Compra'),sg.Input(key='valor', size=(10,1))],
    [sg.Text('Quantidade'),sg.Input(key='quantidade', size=(4,1))],
    [sg.Button('Cadastrar', size=(12,2))]
]

janela = sg.Window('Cadastro de Produtos', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Cadastrar':
        if valores['vendedor'] == 'Pedro':
            print('Produto Cadastrado com sucesso!')
        else :
            print('Produto não cadastrado')
        
