def leap_year(year):
    if(year % 4 is not 0):
        return False
    if(year%100 is not 0):
        return True
    elif (year%100 is 0 and year%400 is 0):
        return True
    return False