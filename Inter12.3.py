from random import randint
def CarregarLista(Q,a,b):
    '''carrega elemento aleatorios em uma lista'''
    l=[]
    for i in range(Q):
        l.append(randint(1, 1000))
    return l

q =int(input("Digite Quantidade"))
lmin =int(input("Digite limite minino"))
lmax =int(input("Digite limite maximo"))



print ("--Inicio do Programa--")
print("Primeira Lista")
valores =CarregarLista(q,lmin,lmax)
print(f"Lista gerada... {valores}com {q} elementos")

print("Segunda Lista")
valores2 =CarregarLista(q,lmin,lmax)
print(f"Lista gerada... {valores2} com {q} elementos" )

