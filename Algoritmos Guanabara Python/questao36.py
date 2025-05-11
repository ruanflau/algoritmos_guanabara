while True:
    horas_ativas = int(input("Quantas horas de atividade física você teve neste mês? "))

    if horas_ativas <= 10:
        pontos = horas_ativas*5
        print("Você ganhou",pontos,"pontos.")
    elif horas_ativas >= 10 and horas_ativas <= 20:
        pontos = horas_ativas*10
        print("Você ganhou",pontos,"pontos.")
    elif horas_ativas < 20:
        pontos = horas_ativas*10
        print("Você ganhou",pontos,"pontos.")
    
    valor = pontos*0.5
    print("O valor a ser pago é: R$ {:.2f}".format(valor))
    
    repetir = input("Deseja calcular outra quantidade de pontos? (s/n): ").lower()
    if repetir != 's':
        print("Encerrando o programa.")
        break