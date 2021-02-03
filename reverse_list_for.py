def reverse_list(A):
    length = len(A)
    for i in range(length//2):
        A[i],A[length-1-i] =  A[length-1-i],A[i]
    print(A)

x = [2,4,7,9,33]
y = [56,76,34,97]
reverse_list(x)
reverse_list(y)
