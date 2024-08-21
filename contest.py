#failed code :(
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    hashh={}
    for j in range(n):
        hashh[l[j]]=j
    p=0;ind=1;lis=[]
    h=max(l)
    while len(hashh)>1:
        for k in hashh:
            mi=hashh[k]
            break
        for k1 in hashh:
            if mi>hashh[k1]:
                mi=hashh[k1]
        max1=0;min1=h;f=0
        for m in range(p,mi+1):
            if ind%2==1:
                if max1<=l[m] and l[m] in hashh:
                    max1=l[m]
                    p=m+1
                    f=1
            else:
                if min1>=l[m] and l[m] in hashh:
                    min1=l[m]
                    p=m+1
        if ind%2==1:
            lis.append(max1)
            del hashh[max1]
        elif ind%2==0:
            lis.append(min1)
            del hashh[min1]
        ind+=1
    for k in hashh:
        lis.append(k)
    print(len(lis))
    for j in range(len(lis)):
        print(lis[j],end=' ')
    print()