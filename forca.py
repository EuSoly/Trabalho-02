
palavra = "atum"
guest = ""
def forca(tentativa):

    f1 = "    +--------+  "
    f2 = "    |           "
    f3 = "    |           "
    f4 = "    |           "
    f5 = "    |           "
    f6 = "    |           "
    f7 = "    |           "
    f8 = "____|____       "
    guest = input("fgfgfgf")
    
    
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
    

def tent(tent):
    sim = input("Deseja jogar? S/N:\n")
    if sim.lower() == "s":
        return forca
    else:
        print("Então vá pa puta que pariu")
tent(0)
