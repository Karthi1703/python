def age_classify():
    while True:
        try:
            age = int(input("Enter Your Age: "))
            if age < 18 :
               print("Minor")
            elif age>=18 & age<=65 :
               print("Adult")
            break
        except ValueError:
               print("Enter valid number")
age_classify()