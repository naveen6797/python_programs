def reverse_number(num):
    result = 0
    for i in range(num):
        if num > 0:
            result1 = num%10
            result = (result*10)+result1
            num = num//10
        else:
            break
    print(result)

reverse_number(345)
reverse_number(864)
