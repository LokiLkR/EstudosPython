import Pacote.utils_bool
import Pacote.utils_txt

print('-'*20)
for s in dir():
    if"__" not in s:
        print(s)
print('-'*20)

a=16
print(Pacote.utils_bool.texto)
r= Pacote.utils_bool.primo(a)
print(f"{a} é primo? {r}")
r =Pacote.utils_bool.paridade(a)
print(f"{a} é par? {r}")

print(Pacote.utils_txt.texto)
Pacote.utils_txt.primo(a)
Pacote.utils_txt.paridade(a)
print("FIM")