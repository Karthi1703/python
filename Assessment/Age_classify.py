def age_classify():
    age = int(input("Enter Your Age: "))
    if age < 18 :
        print("Minor")
    elif age>=18 & age<=65 :
        print("Adult")
    else:
        print("invalid input")
age_classify()