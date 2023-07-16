import random
from time import sleep
import os

os.system("cls")
print("-" *30)
print("BEM-VINDO AO JOGO DO VIRCS")
print("-" *30)
perguntinha = str(input("Você deseja começar o jogo ? (sim/nao): "))
if perguntinha == "sim":    
    computador = ['pedra', 'papel', 'tesoura']
    n = random.choice(computador)

    pergunta2 = str(input("Escolha: pedra, papel, tesoura: "))
    os.system("cls")
    print("CARREGANDO.")
    sleep(1)
    os.system("cls")
    print("CARREGANDO..")
    sleep(1)
    os.system("cls")
    print("CARREGANDO...")
    sleep(1)

    if n == "papel":
        if pergunta2 == "tesoura":
            print(f"O computador escolheu {n} e você {pergunta2}. Você ganhou !!!")
        if pergunta2 == "pedra":
            print(f"O computador escolheu {n} e você {pergunta2}. Você perdeu, tente novamente !!!")
        if pergunta2 == "papel":
            print(f"O computador escolheu {n} e você {pergunta2}. Ouve um empate !!!")

    if n == "pedra":
        if pergunta2 == "tesoura":
                print(f"O computador escolheu {n} e você {pergunta2}Você perdeu, tente novamente !!!")
        if pergunta2 == "papel":
            print(f"O computador escolheu {n} e você {pergunta2}. Você ganhou !!!")
        if pergunta2 == "pedra":
            print(f"O computador escolheu {n} e você {pergunta2}. Ouve um empate !!!")

    if n == "tesoura":
        if pergunta2 == "tesoura":
            print(f"O computador escolheu {n} e você {pergunta2}. Você empatou !!!")
        if pergunta2 == "pedra":
            print(f"O computador escolheu {n} e você {pergunta2}. Você perdeu, tente novamente !!!")
        if pergunta2 == "papel":
            print(f"O computador escolheu {n} e você {pergunta2}. Você ganhou !!!")
if perguntinha == "nao":
    print("Obrigado.")