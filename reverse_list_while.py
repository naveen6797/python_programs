def reverse_list(A):
    i = 0
    length = len(A)
    while (length//2)> i:
        A[i],A[length-1-i]=A[length-1-i],A[i]
        print(A)
        i = i+1

x = [23,65,76,98,32,55]
y = [20,30,40,50,60,70]
reverse_list(x)
reverse_list(y)
