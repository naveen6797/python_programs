def minimum_value(A):
    minimum_value = A[0]
    for i in range(1,len(A)):
        if A[i] < minimum_value:
            minimum_value = A[i]

    print("minimum value of list is::",minimum_value)

x = [34,22,56,7,90]
y = [22,65,87,97,20]
minimum_value(x)
minimum_value(y)
