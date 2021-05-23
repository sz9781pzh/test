def com(list,m,s,e,n):
    if (m==n):
        print(list)
    else:
        for i in range(s,e+2+m-n):
            list[m]=i
            com(list,m+1,i+1,e,n)

l1=[0,0,0]
com(l1,0,1,20,3)