import math
N = float(6)
S = float(1)

#Iterating uptil N is 96 sides
for i in range(2,7):
    d = math.sqrt(1 - pow(S/2,2))
    a = 1 - d
    NewS = math.sqrt(pow(a,2) + pow(S/2,2))
    Perimeter = float(N * S)
    Pi = Perimeter/2
    print(Pi)
    S = NewS
    N = N*2.0
