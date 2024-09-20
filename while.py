# Tupla de frutas
frutas = ('maçã', 'banana', 'laranja', 'uva', 'limão', 'melancia', 'abacaxi',\
          'kiwi', 'manga', 'cereja', 'pêssego', 'pêra', 'figo', 'coco', 'tangerina', 'framboesa', 'morango')

# Inicializa o índice
indice = 0

# Solicita ao usuário que indique uma fruta
fruta_desejada = input("Digite o nome da fruta que deseja encontrar: ")

# Forma de busca em uma lista com o Python
# if fruta_desejada in frutas:
#     print("A fruta desejada foi encontrada na posição: "+str(frutas.index(fruta_desejada)))
# else:
#     print("A fruta desejada não foi encontrada na lista")




fruta_foi_encontrada = False

# Loop while para percorrer a lista
while indice < len(frutas):
    if frutas[indice] == fruta_desejada:
        print("A fruta desejada foi encontrada na posição: "+str(indice))
        fruta_foi_encontrada = True
        break
    print(frutas[indice])
    indice += 1

if not fruta_foi_encontrada:
    print("A fruta desejada não foi encontrada na lista")    