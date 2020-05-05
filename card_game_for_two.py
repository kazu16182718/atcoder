n=int(input())
l=sorted(list(map(int,input().split())),reverse=True)
alice=0
bob=0
for i in range(len(l)):
    if i%2==0:
        alice+=l[i]
    else:
        bob+=l[i]
print(alice-bob)