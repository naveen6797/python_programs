def prime_number(num):
    for i in range(2,num):
        for j in range(2, i//2):
            if i % j == 0:
                break
        else:
            print(i,end=',')

prime_number(100)
