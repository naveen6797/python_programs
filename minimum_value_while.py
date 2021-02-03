def minimum_value(A):
    minimum_value = A[0]
    index = 1
    while index < len(A):
        if A[index] < minimum_value:
            minimum_value = A[index]
        index = index+1
    print ("minimum value value of list is::",minimum_value )

x = [5,8,3,6,2,9,100,1]
y = [10,49,39,400,20]
minimum_value(x)
minimum_value(y)
