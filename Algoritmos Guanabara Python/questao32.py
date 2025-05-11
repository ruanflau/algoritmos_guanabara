#Sorteio de número de 1 a 5
import random
import sys
from random import randint
from sys import platform

#Escolha da máquina
maquina = randint(1, 5)
#Escolha do usuário
usuario = int(input("Em que número de 1 a 5 a máquina pensou? "))

#Verificando se a escolha do usuário é válida
if usuario < 1 or usuario > 5:
    print("Número inválido!")
    sys.exit()

#Mostrando as escolhas 
print(f"\nVocê escolheu: {usuario}")
print(f"A máquina escolheu: {maquina}\n")

#Verificando quem ganhou
if usuario == maquina:
    print("Você ganhou!")
elif usuario > maquina:
    print("Você perdeu!")
else:
    print("Você perdeu!")
