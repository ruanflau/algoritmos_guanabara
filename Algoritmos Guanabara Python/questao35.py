while True:
    tipo_de_carro = input("Qual o tipo de carro que foi alugado? Popular ou De Luxo? ")
    dias = int(input("Por quantos dias o carro foi alugado? "))
    quilometragem = float(input("Quantos quilômetros o carro percorreu? "))

    if tipo_de_carro == "Popular" and quilometragem <= 100:
        valor = (dias * 90) + (quilometragem * 0.2)
    elif tipo_de_carro == "Popular" and quilometragem > 100:
        valor = (dias * 90) + (quilometragem * 0.1)
    elif tipo_de_carro == "De Luxo" and quilometragem <= 200:
        valor = (dias * 150) + (quilometragem * 0.3)
    elif tipo_de_carro == "De Luxo" and quilometragem > 200:
        valor = (dias * 150) + (quilometragem * 0.25)
    else:
        print("Tipo de carro inválido. Tente novamente.")
        continue  # volta pro início do loop

    print("O valor a ser pago é: R$ {:.2f}".format(valor))

    repetir = input("Deseja calcular outro aluguel? (s/n): ").lower()
    if repetir != 's':
        print("Encerrando o programa.")
        break