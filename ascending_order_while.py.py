def ascending_order(a):
    i=0
    while i < len(a):
        j = i+1
        while j < len(a):
            if a[i] > a[j]:
                x = a[i]
                a[i] = a[j]
                a[j] = x
            j = j+1
        i = i+1
    print(a)
        
y = [24,54,87,19,20,9]
z = [34,54,67,2,4,8,99]
ascending_order(y)
ascending_order(z)
