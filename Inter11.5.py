lst = []


for linha in open('saida_er_11.3.txt', 'r'):
    lst.append(float(linha))

print ("lista lida do Arquivo")
print(lst)
Soma=sum(lst)
print(f"Soma dos valores = {Soma}")
Q=len(lst)
print(f"Quantidade = {Q}")
print(f"Media dos valores= {Soma/Q}")
minimo= min(lst)
print(f"Minimo valor = {minimo}")
Max =max(lst)
print(f"Maximo valor = {Max}")