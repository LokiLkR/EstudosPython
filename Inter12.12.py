def funcao1():
    print('dentro da função 1 temos >>> ',a, b)


def funcao2():
    a=100 # escopo local
    b=200
    print('dentro da função 2 temos >>>>', a, b)
# escopo global
a=10
b=20
funcao1()
funcao2()
print('fora das funções temos >>>', a, b)

