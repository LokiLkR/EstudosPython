def fatorial(n):
    if n <=1:
        return 1
    else:
        return n * fatorial(n-1)

entrada = int(input('Digite um inteiro: '))
f= fatorial(entrada)
print(f'O fatorial de {entrada} é {f}')
