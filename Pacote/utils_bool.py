texto = 'Neste modulo as funções retornam um booleano'

def paridade(valor):
    '''c for  PAR'''
    if valor % 2==0:
        return True
    else:
        return False

def primo (valor):
    """c  for PRIMO"""
    if valor ==2:
        return True
    elif valor % 2 ==0:
        return False
    else:
        raiz = pow(valor, 0.5)
        i=3
        while i <= raiz:
            if valor % i ==0:
                return False
            i+=2
        return True
