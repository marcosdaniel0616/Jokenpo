from random import choice
from time import sleep
while True:
    opcoes = ['Pedra', 'Papel', 'Tesoura']
    jogador = ''
    print('Bem vindo!!')
    print('Você irá jogar Jokenpô')
    print('-'*15)
    computador = choice(opcoes)
    while jogador not in opcoes:
        jogador = str(input('Escolha entre pedra, papel e tesoura: ')).capitalize()
    print('Jo')
    sleep(0.75)
    print('Ken')
    sleep(0.75)
    print('Pô')
    sleep(0.50)
    print(f'O jogador jogou {jogador} e o computador jogou {computador}')
    if jogador == 'Pedra':
        if computador == 'Pedra':
            print('EMPATE!')
        elif computador == 'Papel':
            print('VOCÊ PERDEU! :(')
            print('TENTE NOVAMENTE')
        else:
            print('VOCÊ VENCEU!!')
            print('Parabéns!!')
    elif jogador == 'Papel':
        if computador == 'Papel':
            print('EMPATE!')
        elif computador == 'Tesoura':
            print('VOCÊ PERDEU! :(')
            print('TENTE NOVAMENTE!')
        else:
            print('VOCÊ VENCEU!!')
            print('Parabéns!!')
    elif jogador == 'Tesoura':
        if computador == 'Tesoura':
            print('Empate')
        elif computador == 'Pedra':
            print('Você perdeu! :(')
            print('Tente novamente!')
        else:
            print('VOCÊ VENCEU!!')
            print('Parabéns!!!')
    print('-'*20)
    continuar = str(input('Deseja jogar novamente? (s/n): ')).upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja jogar novamente? (s/n): ')).upper()
    if continuar == 'N':
        break