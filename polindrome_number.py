def polindrome_number(number):
    num = number
    result = 0
    for i in range(num):
        if num>0:
            result1 = num%10
            result = (result*10)+result1
            num = num//10
        else:
            break
    print(result)
    if result == number:
        print(number,"its polindrome")
    else:
        print(number,"its not polindrome")
x = 456
y = 232
polindrome_number(x)
polindrome_number(y)
