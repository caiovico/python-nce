# Lista de frutas
basket = []

frutas = ('maçã', 'banana', 'laranja', 'uva', 'limão', 'melancia', 'abacaxi')

# Loop for para iterar sobre a lista
for fruta in frutas:
    print(fruta +" adicionada a cesta")
    basket.append(fruta)

print("Cesta: "+str(basket))