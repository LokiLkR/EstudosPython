def geradorPrimo():
    yield 2
    v= 3
    while True:
        raiz = v** 0.5
        i =3
        while i<= raiz and v % i != 0:
            i+=2
        if i > raiz:
            yield v
        v +=2


gen = geradorPrimo()
Q= int(input('Digite a Quantidade: '))
for _ in range(Q):
    print(next(gen), end = " ")
print("\nFIM")