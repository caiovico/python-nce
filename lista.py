# Como vimos anteriormente, as listas são um tipo de dado que pode armazenar vários valores. 
# Além disso as listas são mutáveis, ou seja, podemos adicionar, remover e alterar valores de uma lista. 
print("Atributo de lista: ")
exemplo_de_lista = []
print(dir(exemplo_de_lista))

# As listas podem ser usadas para armazenar qualquer tipo de dado, inclusive outras listas.
lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for lista in lista_de_listas:
    print(lista)