def fatorial():
    num, fat = 0,1
    while True:
        i = (yield num, fat)
        num+=1
        fat *=num
        if i is not None:
            num , fat = i, 1
            for a in range(1, num +1):
                fat *= num

Q= int(input("Digite qauntidade: "))
gen = fatorial()
next(gen)
n= int(input("\nDigite primeiro fatorial: "))
while n>=0:
    r=gen.send(n)
    fatoriais=[r]
    for _ in range(Q-1):
        fatoriais.append(next(gen))
    print (f"\nSequencia de Fatoriais começado em {n}")
    print(fatoriais)

    n = int(input("\nDigite primeiro fatorial: "))

print("FIM")