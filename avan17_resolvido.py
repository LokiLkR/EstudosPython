from cap17.modAvan17 import retangulo

ret = retangulo(1,1)
s = input("Digite Base e altura separado por espaço")
while s != 'FIM':
    valores = s.split()
    ret.base = float(valores[0])
    ret.altura = float(valores[1])
    ret.exibe()
    s = input("Digite Base e altura separado por espaço")
