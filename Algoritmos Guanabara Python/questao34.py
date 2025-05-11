altura = float(input("Qual a sua altura em M²? "))
peso = float(input("Qual o seu peso em Kg? "))

imc = peso/(altura*altura)

if imc <= 18.5:
    print ("Você está abaixo do peso recomendado.")
elif imc >= 18.5 and imc <= 25:
    print("Você está no seu peso ideal.")
elif imc > 25 and imc < 30:
    print ("Você está em sobrepeso.")
elif imc > 30 and imc < 40:
    print ("Você está em obesidade.")
elif imc > 40:
    print ("Você está em obesidade mórbida.")