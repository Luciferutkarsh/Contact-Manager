first=5
second=4
for i in range(1,first+1):
    print(i,end=" ")
    for j in range(i):
        print('*',end=" ")
    print(" ")
for row in range(second,0,-1):
    print(row,end=" ");
    for column in range(row+1, 1,-1):
        print('*', end=' ')
    print(" ")