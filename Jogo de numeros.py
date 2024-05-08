import random

#Variaveis
vidas = ()
pontos = int()
play = "sim"
Tadivinhe = ()
erros = ()
jogar = "sim"

#Return de jogar novamete
while jogar.lower() == "sim" or jogar.lower() == "s":

    #Print de dados inicias
    adivinhe = random.randint(0,10)
    vidas = + 5
    print("=======Um número de 0 a 10 foi sorteado=======")
    print("você tem", vidas, "tentativas")

    #Return de erro
    while play.lower() == "sim" or play.lower() == "s":

        #Input de tentativa
        Tadivinhe = int(input("Insira um número entre 0 e 10: \n"))

        #Comparador se o numero é diferente do pedido
        if Tadivinhe < 0 or Tadivinhe > 10:
            print("Você nao escolheu um nùmero entre 0 e 10!!!")

        #Tentativa errada 
        if Tadivinhe != adivinhe:
            vidas = vidas - 1
            erros = + 1
            print("Você errou!!, você tem", vidas, "tentativas restantes. Último numero usado", Tadivinhe)

        #Tentativa Certa
        elif Tadivinhe == adivinhe:
            print("Você acertou!!!")
            print("Sobrou", vidas, "tentativas")
            pontos = pontos + 1
            jogar = input("Você deseja jogar novamente?")
            break

        #Sem vida
        if vidas == 0:
            print("Acabou suas vidas!!")
            print("===========FIM DE JOGO==========")
            jogar = input("Você deseja jogar novamente? ")
            break

        #Request de jogar novamente
        play = input("Você deseja jogar novamente? ")
    if play.lower() == "nao" or play.lower() == "n":
        print("===========FIM DE JOGO==========")
        print("Placar")
        print(pontos, "Acertos")
        print(erros , "Erros")
        break
