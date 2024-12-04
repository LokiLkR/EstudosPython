import Pacote.utils_bool as ub
import Pacote.utils_txt as ut

print('-'*20)
for s in dir():
    if"__" not in s:
        print(s)
print('-'*20)


a=16
print(ub.texto)
r= ub.primo(a)
print(f"{a} é primo? {r}")
r =ub.paridade(a)
print(f"{a} é par? {r}")

print(ut.texto)
ut.primo(a)
ut.paridade(a)
print("FIM")