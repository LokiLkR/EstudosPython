texto = " Neste modulo a s funções são texto"

def  paridade (valor):
    if valor% 2==0:
        print(f"{valor} é PAR")
    else:
        print(f"{valor} é IMPAR")

def primo(valor):
    '''PRIMO ou Não PRIMO'''
    if valor ==2:
        print(f"{valor} é PRIMO")
    elif valor % 2==0:
        print(f"{valor} é Não PRIMO")
    else:
        raiz=pow(valor,0.5)
        resto= i = 3
        while i <= raiz and resto !=0:
            resto =  valor % i
            i  += 2
        if resto != 0:
            print(f"{valor} é PRIMO")
        else:
            print(f"{valor} é Não PRIMO")