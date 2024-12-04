def primo(v):
    '''Se v  vor primo = True, se não eh False'''
    if v ==2:
        return True
    elif v %2 ==0:
        return False
    else:
        raiz =pow(v,0.5) #raiz quadrada de v
        i=3
        while i <= raiz:
            if v % i ==0:
                return False
            i+=2
        return True
n = int(input("Digite um Inteiro: "))
if primo (n):
    print(f'{n} é Pimro')
else:

    print(f'{n} não é Pimro')
print("FIM")
