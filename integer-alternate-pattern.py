INPUT:
6
1 2 3 4 5 6

OUTPUT:
1 
5 6 
2 3 4 

INPUT:
8
152 314 123 434 676 343 786 655

OUTPUT:
152
786 655
314 123 434
676 343

CODE:
n=int(input())
l=listart(map(int,input().split()))
start=0
en=n-1
row=1
while start<=en:
    if row%2!=0:
        for i in range(start,min(start+row,en+1)):
            print(l[i],end=" ")
        start+=row
    else:
        for i in range(max(en-row+1,start),en+1):
            print(l[i],end=" ")
        en-=row
    row+=1
    print()
