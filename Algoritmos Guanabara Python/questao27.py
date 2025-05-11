#Calculo de média da nota do aluno
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

#Calcula a média
media = (nota_1 + nota_2) / 2
if media >= 7:
    print("Aprovado")
elif media >= 5 or media < 6.9:
    print("Recuperação")
elif media < 4.9:
    print("Reprovado")