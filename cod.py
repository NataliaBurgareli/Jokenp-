import random
import time

print ("=" *70)
print ("JOGO = PEDRA, PAPEL, TESOURA")
print ("=" *70)

opcoes = ["pedra","papel","tesoura"]

escolha_jogador = input("Escolha (pedra, papel ou tesoura): ").lower()

if escolha_jogador not in opcoes:
    print ("Escolha inválida, tente novamente!")
else:
    print (f"Sua escolha: {escolha_jogador.upper()}")
    time.sleep(1)
    print ("O computador está escolhento")
    time.sleep(2)

    escolha_computador = random.choice(opcoes)
    print (f"Computador escolheu: {escolha_computador.upper()}")

    if escolha_jogador == escolha_computador:
        print ("EMPATE !")
    elif (escolha_jogador == "pedra" and escolha_computador == "tesoura") or \
        (escolha_jogador == "tesoura" and escolha_computador == "papel") or \
        (escolha_jogador == "papel" and escolha_computador == "pedra"):
        print ("Você ganhou! Parabéns ")
    else:
        print ("Você perdeu!")
