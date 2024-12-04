from idlelib.macosx import addOpenEventSupport


def fg():
    resto=0
    num=2
    while True:
        if num %2==resto:
            dado = (yield num)
            if dado is not None:
                if dado not in (0,1):
                    raise ValueError(f"espera-se 0 ou 1 passado -> {dado}")
                resto = dado
                num=0
        num+=1

gen =fg()
print("gera 5 PARES")
for _ in range(5):
    print(next(gen), end=" - ")

print("\ngera 5 IMPARES")
ret=gen.send(1)
print(ret, end=" - ")
for _ in range(4):
    print(next(gen),end = " - ")
print("FIM")

ret= gen.send(2)