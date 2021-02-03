def polindrome_string(name):
    a=name
    i=len(a)-1
    result=''
    while i>=0:
      result=result+a[i]
      i=i-1
    print(result)
    if name == result:
        print(name, "its polindrome")
    else:
        print(name, "its not polindrome")
x = "naveen"
y = "dad"
polindrome_string(x)
polindrome_string(y)
  
