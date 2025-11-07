# Importa o módulo 'random', que contém funções para gerar valores aleatórios.
# Neste jogo, será usado para escolher uma palavra secreta de forma aleatória.
import random

# --- FUNÇÕES PARA ESCOLHER AS PALAVRAS DE ACORDO COM O TEMA E NÍVEL --- #

def capitais1():
    # Abre o arquivo 'capitais1.txt' em modo de leitura ("r") e o associa à variável 'facil'.
    # O comando 'with open' garante que o arquivo será fechado automaticamente após o uso.
    with open("capitais1.txt", "r") as facil:
        # .readlines() lê todas as linhas do arquivo e devolve uma lista, 
        # onde cada linha é um item da lista.
        palavras = facil.readlines()
    # random.choice(lista) escolhe aleatoriamente um elemento da lista.
    # .strip() remove espaços e quebras de linha no início e no fim do texto.
    # .lower() transforma todas as letras em minúsculas para facilitar a comparação no jogo.
    return random.choice(palavras).strip().lower()

def capitais2():
    with open("capitais2.txt", "r") as medio:
        palavras = medio.readlines()
    return random.choice(palavras).strip().lower()

def capitais3():
    with open("capitais3.txt", "r") as dificil:
        palavras = dificil.readlines()
    return random.choice(palavras).strip().lower()

def animais1():
    with open("animais1.txt", "r") as facil:
        palavras = facil.readlines()
    return random.choice(palavras).strip().lower()

def animais2():
    with open("animais2.txt", "r") as medio:
        palavras = medio.readlines()
    return random.choice(palavras).strip().lower()

def animais3():
    with open("animais3.txt", "r") as dificil:
        palavras = dificil.readlines()
    return random.choice(palavras).strip().lower()

def frutas1():
    with open("frutas1.txt", "r") as facil:
        palavras = facil.readlines()
    return random.choice(palavras).strip().lower()

def frutas2():
    with open("frutas2.txt", "r") as medio:
        palavras = medio.readlines()
    return random.choice(palavras).strip().lower()

def frutas3():
    with open("frutas3.txt", "r") as dificil:
        palavras = dificil.readlines()
    return random.choice(palavras).strip().lower()


# --- FUNÇÕES AUXILIARES --- #

def lin():
    # Imprime uma linha de separação (útil para deixar o visual mais organizado no console)
    print('__' * 15)

def continuar():
    # Pergunta se o jogador quer continuar jogando
    segui = input('Deseja continuar? (s/n): ')  # input() lê um texto digitado pelo usuário
    # .lower() deixa o texto em minúsculo
    # .strip() remove espaços extras
    return segui.lower().strip()


# --- INÍCIO DO JOGO --- #

lin()
print('Olá jogador\nVamos escolher um tema?')
print('1 - Capitais brasileiras\n2 - Animais\n3 - Frutas\n0 - Encerrar o jogo')

# Loop principal para o jogador escolher o tema
while True:
    op = int(input('Digite sua opção: '))  # input() retorna uma string; int() converte para número inteiro

    if op == 0:
        # Se o jogador digitar 0, o jogo encerra
        print('Jogo encerrado.')
        lin()
        break
    
    elif op == 1:
        # Tema: CAPITAIS
        nivel = int(input("Escolha seu nível : 1 (fácil), 2 (médio) ou 3 (difícil): "))
        # Escolhe o arquivo correspondente conforme o nível escolhido
        if nivel == 1:
            palavra_secreta = capitais1()
        elif nivel == 2:
            palavra_secreta = capitais2()
        elif nivel == 3:
            palavra_secreta = capitais3()
        else:
            print("Opção inválida!")
            continue  # volta ao início do loop se o nível for inválido
        break

    elif op == 2:
        # Tema: ANIMAIS
        nivel = int(input("Escolha seu nível : 1 (fácil), 2 (médio) ou 3 (difícil): "))
        if nivel == 1:
            palavra_secreta = animais1()
        elif nivel == 2:
            palavra_secreta = animais2()
        elif nivel == 3:
            palavra_secreta = animais3()
        else:
            print("Opção inválida!")
            continue
        break

    elif op == 3:
        # Tema: FRUTAS
        nivel = int(input("Escolha seu nível : 1 (fácil), 2 (médio) ou 3 (difícil): "))
        if nivel == 1:
            palavra_secreta = frutas1()
        elif nivel == 2:
            palavra_secreta = frutas2()
        elif nivel == 3:
            palavra_secreta = frutas3()
        else:
            print("Opção inválida!")
            continue
        break

    else:
        # Caso o usuário digite uma opção que não existe
        print('Opção inválida. Tente novamente.')


# --- EXECUÇÃO DO JOGO DA FORCA --- #

if op != 0:  # Só inicia o jogo se o usuário não escolheu encerrar
    letras_usuario = []  # Lista para armazenar as letras já tentadas
    chances = 7  # Quantidade de tentativas disponíveis
    ganhou = False  # Controle para saber se o jogador acertou toda a palavra

    print('Você tem', chances, 'chances para descobrir a palavra')

    # Enquanto o jogador ainda tiver chances e não tiver vencido
    while chances > 0 and not ganhou:
        print()
        # Mostra a palavra com as letras adivinhadas e os espaços para as que faltam
        for letra in palavra_secreta:
            if letra in letras_usuario:
                print(letra, end=' ')  # Mostra a letra se o jogador já acertou
            else:
                print('_', end=' ')  # Mostra um underline (_) para letras não adivinhadas
        print()

        tentativa = input('Escolha uma letra: ').lower()  # Lê a letra e converte para minúsculo

        if tentativa in letras_usuario:
            # Caso o jogador repita uma letra já escolhida
            print('Você já escolheu essa letra. Tente novamente.')
            continue  # Volta para o início do loop

        letras_usuario.append(tentativa)  # Adiciona a letra na lista de tentativas

        if tentativa not in palavra_secreta:
            # Se a letra não está na palavra, o jogador perde uma chance
            chances -= 1
            print('❌ Letra incorreta! Você perdeu uma chance.')
        else:
            # Se a letra estiver na palavra
            print('✅ Letra correta!')

        # Verifica se o jogador completou todas as letras da palavra
        ganhou = all(letra in letras_usuario for letra in palavra_secreta)
        # all() retorna True se TODAS as condições forem verdadeiras

        if ganhou or chances == 0:
            # Sai do loop se o jogador ganhou ou perdeu todas as chances
            break

        print('Chances restantes:', chances)

    # --- RESULTADO FINAL --- #
    print()
    if ganhou:
        print(f"🎉 Parabéns, você ganhou o jogo!\nA palavra era '{palavra_secreta}'.")
    else:
        print(f"💀 Você perdeu.\nA palavra era '{palavra_secreta}'.")
    lin()
