while True:
    sexo_funcionario = input("Qual o sexo do funcionário? m para masculino e f para feminino: ")
    salario = float(input("Qual o salário do funcionário? "))
    tempo_empresa = int(input("Quanto tempo de empresa, em anos, tem o funcionário? "))

    if sexo_funcionario == "f" and tempo_empresa < 15:
        aumento = salario * 1.05
        print("O aumento será de 5%.")
    
    elif sexo_funcionario == "f" and tempo_empresa > 15 and tempo_empresa <= 20:
        aumento = salario * 1.12
        print("O aumento será de 12%.")
   
    elif sexo_funcionario == "f" and tempo_empresa > 20:
        aumento = salario * 1.23
        print("O aumento será de 23%.")    
    
    elif sexo_funcionario == "m" and tempo_empresa < 20:
        aumento = salario * 1.03
        print("O aumento será de 3%.")
   
    elif sexo_funcionario == "m" and tempo_empresa > 20 and tempo_empresa <= 30:
        aumento = salario * 1.13
        print("O aumento será de 13%.")
    
    elif sexo_funcionario == "m" and tempo_empresa > 30:
        aumento = salario * 1.25
        print("O aumento será de 25%.")

    print("O valor a ser pago é: R$ {:.2f}".format(aumento))
    
    repetir = input("Deseja calcular outro aumento de um funcionário(a)? (s/n): ").lower()
    if repetir != 's':
        print("Encerrando o programa.")
        break