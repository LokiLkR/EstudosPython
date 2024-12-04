class retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calc_area(self):
        return self.base * self.altura

    def exibe(self):
        print(f"rtangulo ({self.base} x {self.altura})")
        print(f"Area = {self.calc_area()}")

r1 = retangulo(12, 5)
print("r1: ", end ='')
r1.exibe()
r2 = retangulo(3.5, 9.0)
print("\nr2: ", end ='')
r2.exibe()

r2.base = 9.5
r2.altura = 16.3
print(f'\n Novo r2 base {r2.base} x altura {r2.altura}')
area = r2.calc_area()
print(f"Nova area de r2 {r2.calc_area()}")
