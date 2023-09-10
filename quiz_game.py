count = 0

nome = input("Digite seu nome: ")

print(f"Olá {nome}! ")

jogar = input("Deseja jogar? (sim/não): ")

if jogar.lower() != "sim":
    quit(print("Tchau! "))
    
else:
    if jogar.lower() == "sim":

        print(f"OK {nome}, vamos começar!")
        
        resposta = int(input("Quanto é 1 + 1: "))

        if resposta == 2:
            count += 1

        resposta = int(input("Quanto é 2 x 2: "))

        if resposta == 4:
            count += 1

        resposta = int(input("Quanto é 10 / 2: "))

        if resposta == 5:
            count += 1
        
        desejo = input(f"Deseja ver sua pontuação? sim/não: ")

        if desejo.lower() != "sim":
            quit(print("Tchau! "))

        else: 
            if desejo.lower() == "sim":
                print(f"Sua pontuação foi: {count}! ")
                
                porcentagem = count / 3 * 100
                porcentagem_format = "{:.2f}".format(porcentagem)

                print(f"Você acertou {porcentagem_format}% das perguntas! ")


            










