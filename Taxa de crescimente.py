A = 200
B = 2000
A1 = 1.5
B1 = 3.0
Av = int()

while A < B:
    A = A * A1
    Av = Av + 1
while A > B:
    print("Com", A, "Habitantes")
    print("Precisou de", Av, "Anos para chegar á população de B" )
    break
