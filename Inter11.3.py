lista=[]
x= (input("Digite Numero: "))
while x !='0':
    lista.append(f"{x}\n")
    x = (input("Digite Numero: "))

arq = open ('saida_er_11.3.txt','w')
arq.writelines(lista)
arq.close()