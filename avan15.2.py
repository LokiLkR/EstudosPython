def fatorial():
    num, fat = 1,1
    while True:
        yield num, fat
        num+=1
        fat *=num



gen = fatorial()
n= int(input("Digite qauntidade:"))
for _ in range(n):
    print(next(gen))
print("FIM")

