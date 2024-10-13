denominators = [1,2,3,4,0,5] #ZERODIVISION ERR

number = 100
for denom in denominators:
    try:
        result = number/denom
        print(result)
    except ZeroDivisionError:
        print("Caught an exception")


