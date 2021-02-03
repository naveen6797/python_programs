def sorting_list(a):
    for i in range(len(a)):
        x = i
        for j in range(i+1, len(a)):
            if a[x] > a[j]:
               x=j
           
        a[i],a[x] = a[x],a[i]
    print(a)

x = [3,6,2,9,5]
y = [4,8,2,5,9]
sorting_list(x)
sorting_list(y)
