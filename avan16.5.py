def soma(a,b):
    print("parte 3 - Namespace Local do python built-in")
    print(dir())
    return a+b

def diferenca(x,y):
    print("parte 3 - Namespace Local do python built-in")
    print(dir())
    return x-y

print("parte 1 - Namespace do python built-in")
print(dir(__builtins__))

print("parte 2 - Namespace Global do python built-in")
v1=8
v2=-36

for a  in dir():
    if "__" not in a:
        print(a)
rs = soma (v1, v2)
print(f"\n{v1}+ {v2}={rs}")

rd = diferenca(v1, v2)
print(f"\n{v1}- {v2}={rd}")