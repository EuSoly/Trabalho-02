import random

def Sorteio(palavras):
    palavras = ["none", "arroz", "atum", "bolacha", "cozinha", "laranja", "espinafre", "matematica", "morango", "teclado", "paralelepipedo" ]
    sorter = random.randint(1,10)
    palavra = (palavras[sorter])
    print(palavra)
    


def forca(tentativa):
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
        print(f5)

def tent(tent):
    sim = input("Deseja jogar? S/N:\n")
    if sim.lower() == "s":
        forca(0)
    else:
        print("Então vá pa puta que pariu")


tent(0)
Sorteio(0)

