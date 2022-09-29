import random as r
import os
import time

lista_palavras = ['extorsao', 'sequestro', 'furto', 'roubo', 'tom', 'gato', 'palavra', 'analise', 'comum', 'proprio', 'advogado', 'material', 'formal']

nome = input('oie, qual seu nome?')
print(f'Olá {nome}!, Seja bem-vinde ao jogo da Forca! :D')
input('\nPressione enter para começar!')
os.system('cls')

palavra_selecionada = r.choice(lista_palavras).upper()
tamanho_palavra = len(palavra_selecionada)
palavra_codificada = ['_']*tamanho_palavra
quantidade_de_erros  = 0

while '_' in palavra_codificada and quantidade_de_erros < 6:
    print(f'\nSua palavra tem {tamanho_palavra} letras.')
    print(f'Erros: {quantidade_de_erros} de 6')
    for letra in palavra_codificada:
        print(letra , end = ' ') # _ _ _ _ 
    print()

    letra_escolhida = input ('Digite uma letra: ').upper()
    acertou = False
    for i in range(len(palavra_selecionada)):
        if letra_escolhida == palavra_selecionada[i]:
            palavra_codificada [i] = letra_escolhida
            acertou = True
    if acertou == True:
        print('Boa! Acertou!')
    else:
        print('Vacilo, não tem essa letra na palavra')
        quantidade_de_erros = quantidade_de_erros + 1

if quantidade_de_erros == 6:
    print('voce perdeu...')
else:
    print('parabens!! voce ganhou :D')

'''for i in range(len(palavra_selecionada)):
    lista_letras.append(palavra_selecionada[i].lower())

for i in range(len(palavra_selecionada)):
    lista_apresentacao.append('_')


def tela():
    print(f'Você so pode errar {erros} vezes até acertar a palavra!')
    
    if len(lista_acertos) > 0:
        for i in range(len(lista_acertos)):
            numElementos = lista_letras.count(lista_acertos[i])
            for elemento in range(numElementos):
                indice = lista_letras.index(lista_acertos[i])
                lista_letras.pop(indice)
                lista_letras.insert(indice, '$')
                lista_apresentacao.pop(indice)
                lista_apresentacao.insert(indice, lista_acertos[i])

    # for i in range(len(lista_apresentacao)):
    #     print(lista_apresentacao[i])

    print(lista_apresentacao)


def tentativa(letra):
    if palavra_selecionada.lower().find(letra) != -1:
        if (lista_acertos.__contains__(letra)):
            print('Essa letra já foi')
            # print(lista_acertos)
        else:
            lista_acertos.append(letra)
            print(f'Woow!, A letra {letra} existe na sua palavra! Muito bem !')

        return 0
    else:
        if (lista_erros.__contains__(letra)):
            print(f'Essa letra já foi')
            return 0
        else:
            lista_erros.append(letra)
            print(
                f'Ahhh. A letra {letra} não existe na sua palavra. :( Tente novamente!')
            return 1

def bonecoErro():
    if erros == 6:
        print('_______ ')
        print('|   o   ')
        print('|       ')
        print('|       ')
        print('|______ ')
    elif erros == 5:
        print('_______ ')
        print('|   o   ')
        print('|   |   ')
        print('|       ')
        print('|______ ')
    elif erros == 4:
        print('_______ ')
        print('|  \o   ')
        print('|   |   ')
        print('|       ')
        print('|______ ')
    elif erros == 3:
        print('_______ ')
        print('|  \o/  ')
        print('|   |   ')
        print('|       ')
        print('|______ ')
    elif erros == 2:
        print('_______ ')
        print('|  \o/  ')
        print('|   |   ')
        print('|    \  ')
        print('|______ ')
    elif erros == 1:
        print('_______ ')
        print('|  \o/  ')
        print('|   |   ')
        print('|  / \  ')
        print('|______ ')

    print(f'Letras erradas: {lista_erros}')
        
def acertou():
    if (lista_letras.count('$') == len(palavra_selecionada)):
        os.system('cls')
        time.sleep(1)
        print('Você acertou a palavra, PARABENS!!!')
        print(f'A palavra era {palavra_selecionada}!')
        return True
    else:
        return False

saudacao()

i = 1
while i <= erros:
    #palavraEscolhida()
    quantidade_de_letras()
    tela()
    bonecoErro()
    if acertou():
        break

    letra = input('Escolha uma letra:')
    erros -= tentativa(letra.lower())
    time.sleep(2)
    os.system('cls')

if (erros == 0):
    print('_______ ')
    print('|   |   ')
    print('|   o   ')
    print('|  /|\   ')
    print('|  | |  ')
    print('|______ ')
    print(f'Que pena você errou! Tente novamente')
    time.sleep(2)
'''