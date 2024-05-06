voltar = ("sim")

#Primeira pessoa
print("=======PRIMEIRA PESSOA======")
nome1 = input("Digite seu Nome: ")
idade1 = int(input("Digite sua idade: "))
sexo1 = input("Digite sua sexualidade: ")
print("Sua ficha foi salva como numero 1!!\n")

#Segunda pessoa
print("=======SEGUNDA PESSOA======")
nome2 = input("Digite seu Nome: ")
idade2 = int(input("Digite sua idade: "))
sexo2 = input("Digite sua sexualidade: ")
print("Sua ficha foi salva como numero 2!!")

#Terceira pessoa
print("=======TERCEIRA PESSOA======")
nome3 = input("Digite seu Nome: ")
idade3 = int(input("Digite sua idade: "))
sexo3 = input("Digite sua sexualidade: ")
print("Sua ficha foi salva como numero 3!!")

#Return de pedido de fichas
while voltar.lower() == "sim":

    #Ficha pessoal
    ficha = (input("Digite o numedo da ficha da pessoa que deseja pegar: "))

    #COmparador de idades
    if idade1 >= 18:
        maior1 = "Você é maior de idade"
    elif idade1 < 18:
        maior1 = "Você é menor de idade"

    if idade2 >= 18:
        maior2 = "Você é maior de idade"
    elif idade2 < 18:
        maior2 = "Você é menor de idade"
        
    if idade3 >= 18:
        maior3 = "Você é maior de idade"
    elif idade3 < 18:
        maior3 = "Você é menor de idade"

    #Print de fichas
        #Ficha 1
    if ficha == "1":
        print("------------------------")
        print("Seu nome é", nome1)
        print("Você tem" , idade1 , "anos")
        print("E sua sexualidade é" , sexo1)
        print(maior1)
        print("------------------------")
        #Ficha 2
    elif ficha == "2":
        print("------------------------")
        print("Seu nome é", nome2)
        print("Você tem" , idade2 , "anos")
        print("E sua sexualidade é" , sexo2)
        print(maior2)
        print("------------------------")
        #Ficha 3
    elif ficha == "3":
        print("------------------------")
        print("Seu nome é", nome3)
        print("Você tem" , idade3 , "anos")
        print("E sua sexualidade é" , sexo3)
        print(maior3)
        print("------------------------")
    
    #Return checker
    voltar = input("Você deseja pegar outra ficha? \n")
    if voltar.lower() == "nao" or voltar.lower() == "não":
        print("Programa de fichas fechado")
