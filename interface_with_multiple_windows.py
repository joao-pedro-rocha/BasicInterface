import PySimpleGUI as sg

# Criar janelas e estilos
def janela_login():
    sg.theme('Reddit')
    
    layout = [
        [sg.Text('Nome:')],
        [sg.Input()],
        [sg.Button('Continuar')] 
    ]
    
    return sg.Window('Login', layout = layout, finalize = True)

def janela_pedido():
    sg.theme('Reddit')
    
    layout = [
        [sg.Text('Fazer pedido')],
        [sg.Checkbox('Pizza Pepperoni', key = 'pizza1'), sg.Checkbox('Frango c/ Catupiry', key = 'pizza2')],
        [sg.Button('Voltar'), sg.Button('Fazer pedido')]
    ]
    
    return sg.Window('Pedido', layout = layout, finalize = True)

# Criar janelas iniciais
janela1, janela2 = janela_login(), None

# Criar um loop de elitura de eventos
while True:
    window, event, values = sg.read_all_windows()
    
    # Quando a janela for fechada
    if event == sg.WIN_CLOSED:
        break
    
    # Quando quisermos ir para a proxima janela
    if window == janela1 and event == 'Continuar':
        janela1.hide()
        janela2 = janela_pedido()
        
    
    # Quando quisermos voltar para a janela anterior
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()

    if window == janela2 and event == 'Fazer pedido':
        if values['pizza1'] == True and values['pizza2'] == True:
            sg.popup('Foram solicitados uma Pizza Pepperoni e uma Pizza Frango c/ Catupiry.')
            
        elif values['pizza1'] == True:
            sg.popup('Foi solicitado uma pizza Pepperoni.')
            
        elif values['pizza2'] == True:
            sg.popup('Foi solicitado uma pizza Frango c/ Catupiry.')
            
window.close()
