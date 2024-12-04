produto={}
print("leitura dos dados")
cod=input("digite o codigo do produto: ")
while cod!= '':
    preco= float(input("digite o preço: R$ "))
    produto[cod] = preco
    cod =input(" digite o codigo: ")

print("Fim da leitura dos dados")
print("Preços do produtos")

for cod in produto.keys():
    print(f"Produto {cod}  custa R$ {produto[cod]:6.2f} ")
