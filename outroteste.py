def gerador():
    a = 1
    while True:
        yield a
        a *= 2

gen = gerador()
next(gen)
soma = 0
for n in range(4):
    soma += next(gen)

print(soma)


