def calcDigito(cod):
    s =str(cod)
    peso = 2
    dv=0
    for a in s:
        dv+= peso *int(a)
        peso+=1
    return dv % 7


codigo = int(input("Digite o Codigo: "))
while codigo>0:
    digito = calcDigito(codigo)
    print(f"Codigo: {codigo} - > Digito: {digito}")
    codigo = int(input("Digite o Codigo: "))

print("FIM")
