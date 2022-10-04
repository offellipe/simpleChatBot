import os #módulo que nos permite utilizar a quebra de linha de forma dinâmica em nossas strings/textos com o {os.linesep}

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} Respondo isso de forma conjunta com a minha noiva, pois concordamos que a cantora Iza é a mais linda.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} Indiscutivelmente "The Lord of the Rings"{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome} Porque além de queimar 10 neurônios a cada partida, você não ganha bosta nenhuma ao jogar.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome} Porque me possibilita criar ideias da minha cabeça, está em expansão mundial e tem palavras coloridas na tela{os.linesep}')
    else:
        print('Digite apenas 1, 2, 3 ou 4')

def start():
    # apresentar o chatbot
    print('Olá! Seja bem-vindo')
    #pedir o nome
    nome = input(f'Digite seu nome: {os.linesep}')
    #pedir email
    email = input(f'Digite seu e-mail: {os.linesep}')
    while True: #criando um loop para refazer o processo caso o usuário queira refazer a pergunta
    # oferecer o menu de opções
        resposta = input(f'O que gostaria de saber hoje?{os.linesep}[1] - Quem é a cantona mais bonita?{os.linesep}[2] - Qual sua trilogia favorita?{os.linesep}[3] - Por que LOL é o pior jogo do mundo?{os.linesep}[4] - Por que ama tecnologia?{os.linesep}')
    # processar a resposta enviada
        processar_resposta(resposta, nome) # aqui referenciamos a função processar_resposta que criamos antes da função start()



if __name__ == '__main__':
    start() #esse if basicamente diz para a nossa aplicação, que quando ela iniciar, deve rodar a função start() que começa na linha 15
