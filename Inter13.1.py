precos=[]
print("Forneça os preços para lista")
preco = float(input("Digite um valor: "))
while preco !=0:
    precos.append(preco)
    preco = float(input("Digite um valor: "))
print("os Preços são estes: ")
print(precos)

aumento = float(input("Digite a porcentagem de aumento: "))
Novosprecos =[valor * (1+ aumento/100) for valor in precos]
for valor in Novosprecos:
    print(f"{valor:.2f}")
print ("FIM")