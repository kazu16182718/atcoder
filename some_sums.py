n,a,b=map(int,input().split())
ans=0
for i in range(1,n+1):
    sum=0
    num=i
    for _ in range(len(str(i))):
        sum+=int(num%10)
        num/=10
    if a<=sum<=b:
        ans+=i
print(ans)