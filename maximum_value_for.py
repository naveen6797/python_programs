def maximum_value(A):
    maximum_value = A[0]
    for i in range(1,len(A)):
        if A[i] > maximum_value:
            maximum_value = A[i]

    print("maximum value of a list is::",maximum_value)

x = [34,22,56,7,90]
y = [22,65,87,97,20]
maximum_value(x)
maximum_value(y)
