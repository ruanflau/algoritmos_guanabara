#Pedra-Papel-Tesoura
import random
import sys
from random import randint
from sys import platform

#Definindo os itens
itens = ["Pedra", "Papel", "Tesoura"]

#Jogada do computador
computador = random.choice(itens)

#Jogada do usuário
usuario = input("Escolha Pedra, Papel ou Tesoura: ").capitalize()

#Verificando se a jogada do usuário é válida
if usuario not in itens:
    print("Jogada inválida!")
    sys.exit()

#Mostrando as jogadas
print(f"\nVocê escolheu: {usuario}")
print(f"O computador escolheu: {computador}\n")

#Verificando quem ganhou
if usuario == computador:
    print("Empate!")
elif (usuario == "Pedra" and computador == "Tesoura") or (usuario == "Papel" and computador == "Pedra") or (usuario == "Tesoura" and computador == "Papel"):
    print("Você ganhou!")   
else:
    print("Você perdeu!")

