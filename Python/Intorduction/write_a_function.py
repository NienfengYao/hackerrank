def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year%4 == 0):
        if (year%100 == 0):
            if (year%400 == 0):
                return True;         
            return False
        return True
    return leap

year = int(input())
print(is_leap(year))
