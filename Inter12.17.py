def leReal(pMin, pMax):
    a = float (input("digite um numero:"))
    while a < pMin or a > pMax:
        print(f'O valor {a} esta fora dos limites [{pMin}, {pMax}]')
        a = float(input("digite um numero:"))
    return a

Lmin = float (input("digite valor Minimo:"))
Lmax = float (input("digite valor Maximo:"))
controle = 's'
while controle == 's' or controle == 'S':
    valor = leReal(Lmin, Lmax)
    print(f"O valor lido é {valor}")
    controle = input("\n Quer digitar outro valor (s/n)???")
print('FIM')
