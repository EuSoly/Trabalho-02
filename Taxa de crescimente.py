
pergunta = "sim"
while pergunta.lower() == "sim" or pergunta.lower() == "s":
    A = int(input("Digite a quantidade de Habitantes do pais A: "))
    B = int(input("Digite a quantidade de Habitantes do pais B: "))
    A1 = float(input("Digite a taxa de crescimento do pais A: "))
    B1 = float(input("Digite a taxa de crescimento do pais B: "))
    Av = int()
    pais = input("Qual pais vc quer o calculo da taxa, Pais A ou Pais B? ")
    A1 = A1 / 100 + 1
    B1 = B1 / 100 + 1
    
    if pais.lower() == "a":
        while A < B:
            A = A * A1 
            Av = Av + 1
            B = B * B1
        while A > B:
            print("Com", int(A), "Habitantes")
            print("Precisou de", Av, "Anos para chegar á população de B" )
            print("Com uma populaçao do pais B de:", int(B), "Habitantes")
            print("Com uma populaçao do pais A de:", int(A), "Habitantes")
            break
    elif pais.lower() == "b":
        while A > B:
            A = A * A1
            Av = Av + 1
            B = B * B1
        while A > B:
            print("Com", int(A), "Habitantes")
            print("Precisou de", Av, "Anos para chegar á população de A" )
            print("Com uma populaçao do pais B de:", int(B), "Habitantes")
            print("Com uma populaçao do pais A de:", int(A), "Habitantes")
    pergunta = input("Deseja fazer o calculo de outro pais? ")
    if pergunta.lower() == "nao" or pergunta.lower() == "n":
        print("=================FIM DO CALCULO================")
