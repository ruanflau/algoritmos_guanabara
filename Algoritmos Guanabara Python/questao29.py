nome_funcionario = input("Digite o nome do funcionário: ")
salario_funcionario = float(input("Digite o salário do funcionário: "))
tempo_servico = int(input("Digite o tempo de serviço do funcionário (em anos): "))

if tempo_servico <= 3:
    print("O novo salário do funcionário é: R$ {:.2f}".format(salario_funcionario * 1.03))
elif tempo_servico > 3 and tempo_servico <= 10:
    print("O novo salário do funcionário é: R$ {:.2f}".format(salario_funcionario * 1.125))
elif tempo_servico > 10:
    print("O novo salário do funcionário é: R$ {:.2f}".format(salario_funcionario * 1.2))
    