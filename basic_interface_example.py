import PySimpleGUI as sg

# Tema da interface
sg.change_look_and_feel('DarkBlue15')

class TelaPython:
    def __init__(self):
        
        # Layout
        layout = [
            
            # Texto e em seguida o campo para digitar.
            # O size regula o espaço de cada elemento na tela.
            # Precisa usar a key (uma espécie de nome) onde houver entrada de dados para armazenar
            # os dados em variaveis.
            [sg.Text('Nome', size = (5, 0)), sg.Input(size = (15, 0), key = 'nome')],
            [sg.Text('Idade', size = (5, 0)), sg.Input(size = (15, 0), key = 'idade')],
            
            # sg.Checkbox cria checkbox com textos
            [sg.Checkbox('Gmail', key = 'gmail'), sg.Checkbox('Outlook', key = 'outlook'), sg.Checkbox('Yahoo', key = 'yahoo')],
            
            [sg.Text('Aceita cartão')],
            
            # sg.Radio cria um check redondo
            [sg.Radio('Sim', 'cartão', key = 'cartaoSim'), sg.Radio('Não', 'cartão', key = 'cartaoNao')],
            
            # Cria um botao deslizante
            [sg.Slider(range = (0, 255), default_value = 0, orientation = 'h', size = (15,20), key = 'sliderVelocidade')],
            
            [sg.Button('Enviar dados')], # Botão com "Enviar dados"
            
            # Cria um campo em branco com o output print do codigo
            [sg.Output(size = (30, 10))]
        ]

        # Janela
        # Usar self.janela para criar um loop
        # e poder usar o mesmo programa mais de uma vez.
        self.janela = sg.Window('Dados do usuário').layout(layout)
        
    def Iniciar(self):
        while True:

        # Extrair dados da tela
            self.button, self.values = self.janela.Read()
                
            nome = self.values['nome']
            idade = self.values['idade']
            gmail = self.values['gmail']
            outlook = self.values['outlook']
            yahoo = self.values['yahoo']
            aceita_cartao = self.values['cartaoSim']
            nao_aceita_cartao = self.values['cartaoNao']
            velocidade_script = self.values['sliderVelocidade']
                    
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Aceita Gmail: {gmail}')
            print(f'Aceita Outlook: {outlook}')
            print(f'Aceita Yahoo: {yahoo}')
            print(f'Aceita cartão: {aceita_cartao}')
            print(f'Não aceita cartão: {nao_aceita_cartao}')
            print(f'Velocidade scripts: {velocidade_script}')
            print(f'=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
                    
            #print(self.values)
        
tela = TelaPython()
tela.Iniciar()
