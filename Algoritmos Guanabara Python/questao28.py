largula_terrero = float(input("Digite a largura do terreno: "))
comprimento_terreno = float(input("Digite o comprimento do terreno: "))
area_terreno = largula_terrero * comprimento_terreno

if area_terreno <= 100:
    print("TERRENO POPULAR")
elif area_terreno > 100 and area_terreno <= 500:
    print("TERRENO MASTER")
elif area_terreno > 500:
    print("TERRENO VIP")