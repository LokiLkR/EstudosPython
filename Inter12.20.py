from time import sleep

def contagem (cont):
    if cont ==0:
        print("NO AR!")
    else:
        print(cont)
        sleep(1)
        contagem(cont-1)


toques = int(input("Digite a quantidade de Toques: "))
print(f"Atenção para o toque de {toques} segundos")
contagem(toques)