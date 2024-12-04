from random import randint
Q=int(input("Digite a Quantidade: " ))
while Q >50:
    print("VAlor muito alto")
    Q=int(input("Digite a Quantidade (50 max): " ))
conjunto =set()
while len(conjunto) < Q:
    conjunto.add(randint(1,50))
print (conjunto)
print(f" o conjunto tem {len(conjunto)} elementos")