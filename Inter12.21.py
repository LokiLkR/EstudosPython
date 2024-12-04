def soma (P,R,Qua):
    if Qua > 0:
        return P + soma(P+R, R, Qua-1)
    else:
        return 0

prim= int(input("Digite termo: "))
razao= int(input("Digite Razão: "))
Q= int(input("Digite Quantidade: "))
resultado = soma(prim, razao, Q)
print(f"par Primeiro = {prim}; Razão ={razao}; Quantidade{Q} ---> Soma {resultado}")