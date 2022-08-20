import random
from time import sleep

def converte_em_lista(arquivo, lista):
    with open(arquivo, 'r', encoding='UTF8') as texto:
        for linha in texto:
            lista.append(str(linha).replace('\n', ''))
        return lista

frases = []
frases = converte_em_lista('ditados.txt', frases)

# Inicio do programa
jogador = input('Informe seu nome: ')
sleep(1)
print(f'É uma honra te conhecer {jogador}')
sleep(1)
print(f'Me chamo Harvey, o seu guru pessoal, pode me perguntar qualquer coisa')
sleep(2)
jogar = True
perguntas = []
while jogar == True:
    print(f'Quer fazer uma pergunta {jogador}?')
    print('Sim (1)')
    print('Não (2)')
    try:
        resposta = int(input('Sua resposta: '))
        if resposta == 1:
            print('Ok, então faça sua pergunta')
            pergunta = input('Sua pergunta: ')
            if pergunta not in perguntas:
                perguntas.append(pergunta)
                print('Hummm...')
                for i in range(5):
                    print('...')
                    sleep(1)
                resposta = frases[random.randint(0, len(frases))]
                print(resposta)
        elif resposta == 2:
            jogar = False
            print(f'Ok, nos vemos em breve!')
    except:
        print('Resposta inválida, tente novamente')