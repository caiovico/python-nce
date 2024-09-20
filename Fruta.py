# Exemplo de classe em Python
# Uma classe é uma estrutura que representa um objeto e suas propriedades.
class Fruta:
    def __init__(self, nome, peso, cor, no_brasil):
        self.nome = nome
        self.peso = peso
        self.cor = cor
        self.nativa_do_brasil = bool(no_brasil)  # Ensure it's a boolean

    def __str__(self):
        return f"Fruta: {self.nome}, Peso: {self.peso}g, Cor: {self.cor}, No Brasil: {'Sim' if self.nativa_do_brasil else 'Não'}"
    


# Pode ser instanciada para criar objetos que possuem as características definidas na classe.
maca = Fruta("Maçã", 150, "Vermelha", True)
banana = Fruta("Banana", 120, "Amarela", True)
print(maca)
print(banana)
