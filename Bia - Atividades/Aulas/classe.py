class pessoa:
    def __init__(self, altura, peso):
        self.altura = altura
        self.peso = peso
    def __str__(self):
        return f'{self.altura}, {self.peso}'
    def __eq__(self, value):
        return self.altura == value.altura and self.peso == value.peso
        pass
    def crescer(self, aumento):
        self.altura += aumento


pessoa1 = pessoa(1.8, 60)
pessoa2 = pessoa(1.9, 80)

pessoa1.crescer(0.5)
print(f"{pessoa1}")

