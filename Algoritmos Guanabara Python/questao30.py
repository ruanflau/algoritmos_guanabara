#Calculadora de triangulos
segmento_a = float(input("Digite o comprimento do primeiro segmento: "))
segmento_b = float(input("Digite o comprimento do segundo segmento: "))
segmento_c = float(input("Digite o comprimento do terceiro segmento: "))

# Verifica se os segmentos podem formar um triângulo
if segmento_a + segmento_b > segmento_c and segmento_a + segmento_c > segmento_b and segmento_b + segmento_c > segmento_a:
    print("Os segmentos podem formar um triângulo.")
    
    # Verifica o tipo de triângulo
    if segmento_a == segmento_b == segmento_c:
        print("O triângulo é equilátero.")
    elif segmento_a == segmento_b or segmento_a == segmento_c or segmento_b == segmento_c:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
else:   
    print("Os segmentos não podem formar um triângulo.")
# Fim do código
