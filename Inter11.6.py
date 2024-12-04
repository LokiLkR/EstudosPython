estoque= {}
for linha in open ('saida_er_11.3.txt', 'r'):
    lst = linha.rstrip().split(';')
    print(lst)
    cod = int(lst[0])
    Q= int(lst[1])
    Pund= float(lst[2])
    estoque[cod] = (Q, Pund)
print(f"Valores carregados no dicionario")
print(estoque)
print("\n TABELA")
totGeral = 0
for cod, dados in estoque.items():
    tot = dados[0] * dados[1]
    totGeral +=tot
    print(f'{cod}: {dados[0]:5d} x {dados[1]:6.2f} = {tot:8.2f}')
print(' ' *24, f'{totGeral:8.2f}')


print("\nFIM")