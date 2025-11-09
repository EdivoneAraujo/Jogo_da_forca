import random

# --- FUNÇÃO GENÉRICA PARA ESCOLHER PALAVRAS --- #
def escolher_palavra(tema, nivel):
    arquivos = {
        "capitais": ["capitais1.txt", "capitais2.txt", "capitais3.txt"],
        "animais":  ["animais1.txt",  "animais2.txt",  "animais3.txt"],
        "frutas":   ["frutas1.txt",   "frutas2.txt",   "frutas3.txt"]
    }

    nome_arquivo = arquivos[tema][nivel - 1]
    with open(nome_arquivo, "r") as arquivo:
        palavras = arquivo.readlines()

    palavra_sorteada = random.choice(palavras).strip().lower()
    return palavra_sorteada


# --- FUNÇÕES AUXILIARES --- #
def lin():
    print('__' * 15)


def continuar():
    return input('Deseja continuar? (s/n): ').lower().strip()


# --- INÍCIO DO JOGO --- #
def jogo_da_forca():
    lin()
    print('Olá jogador!\nVamos escolher um tema?')
    print('1 - Capitais brasileiras\n2 - Animais\n3 - Frutas\n0 - Encerrar o jogo')

    temas = {1: "capitais", 2: "animais", 3: "frutas"}

    # Escolha do tema
    op = -1
    while op not in [0, 1, 2, 3]:
        entrada = input('Digite sua opção: ')
        if entrada in ['0', '1', '2', '3']:
            op = int(entrada)
        else:
            print("Por favor, escolha uma opção válida: 0, 1, 2 ou 3.")

    if op == 0:
        print('Jogo encerrado.')
        lin()
        return

    # Escolha do nível
    nivel = 0
    while nivel not in [1, 2, 3]:
        entrada_nivel = input("Escolha o nível: 1 (fácil), 2 (médio) ou 3 (difícil): ")
        if entrada_nivel in ['1', '2', '3']:
            nivel = int(entrada_nivel)
        else:
            print("Por favor, escolha apenas 1, 2 ou 3.")

    palavra_secreta = escolher_palavra(temas[op], nivel)

    # --- EXECUÇÃO DO JOGO --- #
    letras_usuario = []
    chances = 7
    ganhou = False

    print(f'Você tem {chances} chances para descobrir a palavra.')

    while chances > 0 and not ganhou:
        print()
        for letra in palavra_secreta:
            if letra in letras_usuario:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        print()

        tentativa = input('Escolha uma letra: ').lower().strip()

        # validação manual da letra
        if len(tentativa) != 1:
            print("Digite apenas uma letra.")
            continue
        if tentativa < 'a' or tentativa > 'z':  # valida caractere sem isalpha()
            print("Digite apenas letras de A a Z.")
            continue

        if tentativa in letras_usuario:
            print('Você já escolheu essa letra. Tente novamente.')
            continue

        letras_usuario.append(tentativa)

        if tentativa in palavra_secreta:
            print('✅ Letra correta!')
        else:
            chances -= 1
            print('❌ Letra incorreta! Você perdeu uma chance.')

        # verificar se todas as letras da palavra foram descobertas (sem usar all)
        ganhou = True
        for letra in palavra_secreta:
            if letra not in letras_usuario:
                ganhou = False
                break

        print('Chances restantes:', chances)

    # --- RESULTADO FINAL --- #
    lin()
    if ganhou:
        print(f"🎉 Parabéns! Você ganhou o jogo!\nA palavra era '{palavra_secreta}'.")
    else:
        print(f"💀 Você perdeu.\nA palavra era '{palavra_secreta}'.")
    lin()


# --- EXECUTAR JOGO --- #
if __name__ == "__main__":
    jogo_da_forca()
