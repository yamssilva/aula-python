import os
from time import sleep 
list = {
    "fantasia": ["Harry potter e a pedra filosofal", "O Senhor dos Anéis", "A Canção de Gelo e Fogo"],
    "romance": ["O Castelo Animado", "melhor do que nos filmes", "Orgulho e Preconceito"],
    "distopia": ["O Jardim Secreto", "Jogos Vorazes", " 1984 "],
    "aventura": ["Percy Jackson e os Olimpianos: O Ladrão de Raios", "O Hobbit", "As Aventuras de Huckleberry Finn"],
    "terror": ["Coraline", "It: A Coisa", " O Iluminado "],
    "poesia": ["O menino azul", "O sol é para todos", "Pra você que sente demais "],
}

while True:
    print("""Seja Bem-Vindo(a) ao indicalivros!!
          """)
    print("""------------------------QUADRO DE ESCOLHAS------------------------
          *****selecione uma das seguintes opções a seguir*****

          1. Para: Receber Indicação
          2. Para: Avaliar
          3. Para: Sair 

          """)
    escolha = int(input("Escolha uma das opções (1,2,3) : "))
    if escolha == 3:
        print("Programa encerrado.") 
        break 
    elif escolha == 1:
        gen = input("Digite um gênero entre: fantasia, romance, distopia, aventura, terror, poesia: ")
        idade=int(input("digite sua idade: "))
        livro_escolhido = ""
        if idade < 13:
            livro_escolhido = list[gen][0] # gen é o texto "chave", valor é a lista td
            sleep(0.5)
            os.system("cls")
        elif idade < 18:
            livro_escolhido = list[gen][1]
            sleep(0.5)
            os.system("cls")
        else:
            livro_escolhido = list[gen][2]
            sleep(0.5)
            os.system("cls")

        print(f"""De acordo com a sua faixa etaría e gênero escolhido, uma otima indicação de livro seria: {livro_escolhido}!
              """)

    if escolha == 2:
        nm = input("Digite o nome do livro: ")
        g = input("Digite o gênero do livro: ")
        av = float(input("Avalie o livro de 0 a 5: "))
        if av > 5 or av < 0:
            sleep(0.5)
            os.system("cls")
            print("""erro, tente novamente.
                  """)
        else:
         sleep(0.5)
         os.system("cls")
         print(f"""Agradecemos a sua avaliação do livro {nm}!
                """)
        
