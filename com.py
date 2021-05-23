def combine(list,m,s,e,n):
    if (m==n):
        print(list)
    else:
        for i in range(s,e+2+m-n):
            list[m]=i
            combine(list,m+1,i+1,e,n)

l1=[0,0,0]
combine(l1,0,3,8,3)