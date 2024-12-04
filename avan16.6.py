def funcao1():
    print(".... inicio da função1 ")
    if   criterio == "alterar":
        valor = 999
    print(f"... valor dentro da  função1 = {valor}")

def funcao2():
    print(".... inicio da função2 ")
    global valor
    if   criterio == "alterar":
        valor = 999
    print(f"... valor dentro da  função2 = {valor}")


criterio= "alterar"
valor=10
print(f"programa principal valor = {valor} ANTES da função 1")
funcao1()
print(f"programa principal valor = {valor} APOS da função 1")

print(f"\nprograma principal valor = {valor} ANTES da função 1")
funcao2()
print(f"programa principal valor = {valor} APOS da função 1")