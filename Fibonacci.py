quanto = int(input("quantas casa você quer? "))
fim = 0
numA = 1
numB = 0

while fim < quanto:
    num = numA + numB
    numB = numA 
    numA = num
    print (num)
    fim = fim + 1
