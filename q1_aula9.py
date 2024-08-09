#1questão , aula 9

a = int(input("informe o primeiro núm inteiro: "))
b = int(input("informe o segundo núm inteiro: "))
s = 0
if a < b:
    for x in range(a , b+1):
        s += x
    print (s)

else:
    print("erro!")
