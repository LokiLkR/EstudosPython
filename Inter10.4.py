UF={}
print("leitura dos dados")
while True:
    sigla= input("---- Digite a sigla do Estado: ")
    if sigla == "":
        break
    elif sigla in UF:
        print(f"... {sigla} a sigla ja registrada")
        continue
    estado = input("Digite o nome do Estado: ")
    capital = input("Digite o nome do Catiptal: ")
    pib= float(input("Digite o PIB: "))
    dicitem = {'nome': estado, 'capital': capital,'pib': pib}
    UF[sigla]=dicitem


print("Fim da leitura dos dados")

print("     {:15} {:15} {:>10}" .format ('Estado', 'Capital', 'PIB'))
for sigla, dados in UF.items():
    print("({}) {:15} {:15} {:10.1f} ".format
          ( sigla, dados['nome'], dados['capital'], dados['pib']))