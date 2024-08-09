usuario = input("Digite eu nome:")

err = 0
while err < 3:
    sen = int(input("Digite sua senha: "))
    if sen == 123456:
        print("Oi , seja bem vindo ao banco! ")
        break
    else:
        err += 1 
    if err<3:
        print(f"Senha incorreta! Você ainda tem { 3- err} tentativa")
    else:
        print("Senha senha foi bloqueada! Por favor , dirija-se a um de nossos caixas")
        break    
