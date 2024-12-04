def filtro(dados, pmin, pmax):
    for valor in dados:
        if pmin<= valor <= pmax:
            yield valor, valor* 1.1

precos = [36.3, 174.19, 43.71, 108.32, 89.14]
lmin = int(input ("Digite o valor minimo: "))
lmax = int(input ("Digite o valor maximo: "))
for valores in filtro(precos, lmin, lmax):
    print(valores)
print("FIM")