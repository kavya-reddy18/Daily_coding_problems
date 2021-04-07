def solve(a,n):
    if n==1:
        return 0
    pre=[1]*n
    t=1
    for i in range(n):
        pre[i]=t
        t*=a[i]
    t=1
    for i in range(n-1,-1,-1):
        pre[i]*=t
        t*=a[i]
    return pre
n=int(input())
a=list(map(int,input().split()))
print(solve(a,n))