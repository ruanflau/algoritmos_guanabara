#Calcular se emprestimo para casa é válido
valor_casa = float(input("Digite o valor total da casa: "))
valor_salario = float(input("Digite o valor do salário: "))
tempo_casa = float(input("Digite o tempo esperado para pagar a casa: "))

prestacao_mensal = valor_casa/(tempo_casa*12)
salario_aprovado = (valor_salario/100)*30

if prestacao_mensal >= salario_aprovado:
    print("O emprestismo não foi aprovado.")
else:
    print("O emprestismo foi aprovado.")