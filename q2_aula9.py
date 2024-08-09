#2questão , aula 9

pt = int(input("Digite o primeiro termo: "))
qt = int(input("Digite a quantidade termos: "))
raz = int(input("Digite a razão termo: "))

ultimo_termo = pt + (qt-1)*raz
for termo in range (pt , ultimo_termo +1, raz):
    print(termo)
print("fim")
