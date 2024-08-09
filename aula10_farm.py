#1. Construa um programa que receba o nome e o preço de 5 medicamentos de uma drogaria 
# (considere que o usuário informou cinco medicamentos distintos).
#  O programa deve informar o nome e o preço do medicamento mais barato, bem como a média aritmética dos preços informados
soma_precos = 0

medicamento = input("Digite o nome do medicamento: ")
preco = float(input("Digite o preço: "))

maisbarato = medicamento
menor_preco = preco

soma_precos += preco

for x in range(4):
    medicamento = input("Digite o nome do medicamento: ")
    preco = float(input("Digite o preço: "))
    if preco < menor_preco:
        menor_preco = preco
        maisbarato = medicamento
    soma_precos += preco

media = soma_precos/5
print(f"{maisbarato} é o medicamento mais barato e custa R$ {menor_preco:.2f}.")
print(f"média dos preços: R${media:.2f}.")



