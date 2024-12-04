class retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @property #getter - obter valor add _base(privado)
    def base(self):
        return self._base


    @base.setter #setter - reegatar o q esta em _base
    def base(self, valor):
        if not isinstance(valor, int | float):
            raise TypeError("Valor Numerico")
        if valor <= 0:
            raise ValueError ("Numero positivo esperado!")
        self._base = valor

    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, val):
        if not isinstance(val, int | float):
                raise TypeError("Valor Numerico")
        if val <= 0:
                raise ValueError("Numero positivo esperado!")
        self._altura = val



    def calc_area(self):
        return self.base * self.altura

    def exibe(self):
        print(f"retangulo ({self.base} x {self.altura})")
        print(f"Area = {self.calc_area()}")