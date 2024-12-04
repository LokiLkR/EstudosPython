def Paridade(pValor):

    if not isinstance (pValor, int):
        raise Exception("A Fução espera um Numero Inteiro")
    if pValor % 2==0:
        return "PAR"
    else:
        return "IMPAR"

n= input("Digite algo: ")
r=Paridade (int(n))
print(f"{n} é {r}")

