l=[1,5,10,20, 40, 80]
l1=[6, 7, 20, 80, 100]
l2=[3, 4, 15, 20, 30, 70, 80, 120]

out=set(l1) & set(l2) & set(l)
if(len(out)>0):
    print(' '.join(map(str,out)))
else:
    print(-1)
