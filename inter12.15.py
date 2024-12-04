def paridade(a):
    return 'PAR' if a %2==0 else 'IMPAR'


n= int(input("Digite um interiro: "))
print(paridade(n))
