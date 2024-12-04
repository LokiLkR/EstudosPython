def primo(v):
    '''Se v  vor primo = True, se não eh False'''
    if not isinstance(v, int):
        raise TypeError("Tipo invalido, deve ser um Inteiro")
    if v < 2:
        raise ValueError("Valor invalido, argumento tem q ser no minimo 2")
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

try:
    n = int(input("Digite um Inteiro: "))
    if primo (n):
        print(f'{n} é Primo')
    else:
        print(f'{n} não é Primo')
except TypeError as te:
    print(f"ERRO!!!{te}")
except ValueError as ve:
    print(f"ERRO!!!{ve}")

print("FIM")
