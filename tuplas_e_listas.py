# Title: Tuplas e Listas
# Tuplas são imutáveis e listas são mutáveis
exemplo_de_tupla = "Azul", "Verde", 2
for item in exemplo_de_tupla:
    print(item)

print()
exemplo_de_lista = ["Azul", "Verde", 2]
for item in exemplo_de_lista:
    print(item)

exemplo_de_lista.append("Amarelo")
print()
for item in exemplo_de_lista:
    print(item)

exemplo_de_lista.remove("Verde")

print("Atributo de lista: ")
print(dir(exemplo_de_lista))
print()
print("Atributo de tupla: ")
print(dir(exemplo_de_tupla))
