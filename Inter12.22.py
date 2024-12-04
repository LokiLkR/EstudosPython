def BuscaBin( valor, lista, ini, fim):
    print(f"Inicio = {ini} e Fim = {fim}")
    if ini >fim:
        return False
    meio = (ini+fim)//2
    print(f"Meio = {meio} e o valor nessa posição {lista[meio]}")
    if valor == lista[meio]:
        return True
    elif valor <lista[meio]:
        return BuscaBin(valor, lista, ini, meio-1)
    else:
        return BuscaBin(valor, lista, meio + 1, fim)




L=[14,17,20,22,23,25,28,29,31,35,40,45,50,53,56,59,62,65]
x=int(input("Digite um valor para pesquisa: "))
while x!=0:
    Achou = BuscaBin(x,L, 0, len(L)-1)
    if Achou !=0:
         print(f"{x} esta na Lista")
    else:
        print(f"{x} Não esta na Lista")
    x=int(input("Digite um valor para pesquisa: "))
print("FIM")
