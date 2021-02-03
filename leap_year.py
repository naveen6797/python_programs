def check_year(year):
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                print("{} is a leap year".format(year))
            else:
                print("{} is not a leap year".format(year))
        else:
            print("{} is a leap year".format(year))
    else:
        print("{} is not a leap year".format(year))
check_year(1900)
check_year(2001)
check_year(2004)
