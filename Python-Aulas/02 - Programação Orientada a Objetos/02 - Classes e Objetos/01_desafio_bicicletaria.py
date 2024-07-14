# %%
class Bicicleta:
# Para inicializar os atributos da classe é definido um metodo construtor, e depois colocado os métodos desejado, com o self
# O "Self" representa a instancia do objeto
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

# Métodos são funções dentro de uma classe

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

    def get_cor(self):
        return self.cor

    #def __str__(self):
    #    return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    # OU
    def __str__(self):        
        return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor= {self.valor}"

b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)
b2.correr()
b2.get_cor() #ou print(b2.cor)

# %%
