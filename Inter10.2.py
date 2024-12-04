produto={}
print("leitura dos dados")
while True:
    cod = input(" digite o codigo: ")
    if cod == "":
        break
    elif cod in produto:
        print(f"... {cod} o Codigo ja registrado")
        continue
    preco = float(input("digite o preço: R$ "))
    produto[cod] = preco


print("Fim da leitura dos dados")
print("Preços do produtos")

for cod in produto.keys():
    print(f"Produto {cod}  custa R$ {produto[cod]:6.2f} ")