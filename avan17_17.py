class FormaGeometrica:
    def __init__(self):
        self.tipo_forma ="Forma não definida"

    def exibe_tipo_forma(self):
        print(self.tipo_forma)

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.tipo_forma = "Circulo"
        self.raio = raio

    def exibe_dados(self):
        super().exibe_tipo_forma()
        print(f'detalhes: raio = {self.raio}')

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.tipo_forma = 'Retangulo'
        self.base = base
        self.altura = altura

    def exibe_dados(self):
        super().exibe_tipo_forma()
        print(f'detalhes: raio = {self.base} x {self.altura}')


