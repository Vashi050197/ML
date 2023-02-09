# n=int(input())
# while(n>0):
l=list(map(int,input().split()))
if l[2]<=l[1]:
    print(l[2])
elif l[2]>l[1] and l[2]<=l[0]:
    print(l[1])
else:
    print(l[1]-l[2]+l[0])
            


# n-=1