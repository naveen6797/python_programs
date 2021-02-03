def reverse_number(num):
    result = 0
    while num > 0:
        result1 = num % 10
        result = (result*10)+result1
        num = num//10
    print(result)

reverse_number(452)
reverse_number(647)

