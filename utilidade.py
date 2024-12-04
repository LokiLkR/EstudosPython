texto = 'Modolo ultilidade.py'
meses =['jan', 'fev','mar', 'abr', 'mai','jun'
        'jun','ago','set','out','nov', 'dez']

def paridade(valor):
    if valor % 2==0:
        return 'PAR'
    else:
        return 'IMPAR'

def primo(valor):
    if valor ==2:
        return True
    elif valor  %2==0:
        return False
    else:

        raiz=pow(valor, 0.5)
        i=3
        while i<=raiz:
            if valor % i ==0:
                return False
            i+=2
        return True