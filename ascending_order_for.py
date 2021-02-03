def ascending_order(a):
    for i in range(len(a)):
        x = i
        for j in range(i+1, len(a)):
            if a[x] > a[j]:
               x=j
           
        a[i],a[x] = a[x],a[i]
    print(a)
y = [23,53,2,4,8,98,1,298,6]
z = [33,2,5,7,87,9,432,1]
ascending_order(y)
ascending_order(z)
