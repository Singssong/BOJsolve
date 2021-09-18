E, S, M = map(int,input().split())
count = 0
X=0
Y=0
Z=0

while(1):
    if(X == E and Y == S and Z == M):
        break
    else:
        X = X + 1
        Y = Y + 1
        Z = Z + 1
        if (X == 16):
            X = 1
        if (Y == 29):
            Y = 1
        if (Z == 20):
            Z = 1
        count = count + 1

print(count)
