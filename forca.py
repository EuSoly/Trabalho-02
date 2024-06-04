import random
erros = 0
def Sorteio(palavra):
    palavras = ["none", "arroz", "atum", "bolacha", "cozinha", "laranja", "espinafre", "matematica", "morango", "teclado", "paralelepipedo" ]
    sorter = random.randint(1,10)
    palavra = (palavras[sorter])
    return palavra
def Forca(tentativa):
    f1 = "    +--------+  "
    f2 = "    |           "
    f3 = "    |           "
    f4 = "    |           "
    f5 = "    |           "
    f6 = "    |           "
    f7 = "    |           "
    f8 = "____|____       "

    if tentativa >= 1:
        f2 = f2 = "    |        |  "
        f3 = f3 = "    |        0  "

    if tentativa >= 2:
        f4 = f4 = "    |        |  "

    if tentativa >= 3:
        f4 = f4 = "    |       /|  "
        
    if tentativa >= 4:
        f4 = f4 = "    |       /|\ "

    if tentativa >= 5:
        f5 = f5 = "    |        |  "

    if tentativa >= 6:
        f6 = f6 = "    |       /   "

    if tentativa >= 7:
        f6 = f6 = "    |       / \ "
        
    if tentativa >= 8:
        print("Você perdeu!!")
    
    print(f1)
    print(f2)
    print(f3)
    print(f4)
    print(f5)
    print(f6)
    print(f7)
    print(f8)
    return tentativa
def Tent():
    sim = input("Deseja jogar? S/N:\n")
    if sim.lower() == "s":
        Forca(0)
        
    else:
        print("Então vá pa puta que pariu")

Tent()
while 0 < 9:
    tentativa = input("Digite a palavra")
    if tentativa == Sorteio:
        print("Acertou")
    if tentativa != Sorteio:
        erros = erros + 1
        Forca(erros)

