def temp (temper):
    if temper < 0 :
        print("It's freezing!")
    elif temper >= 0 and temper < 10:
        print("It's cold!")
    elif temper >= 10 and temper < 20:
        print("It's cool!")
    elif temper >= 20 and temper < 30:
        print("It's warm!")
    else: 
        print("It's hot!")
temper = float(input("Enter the temperature in Celsius: "))
temp(temper)