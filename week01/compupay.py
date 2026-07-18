hours = float(input("Hours"))
rate = float(input("rate"))
otrate = rate * 1.5
def pay(hours,rate):
    if hours > 40:
        pay = (40*rate) + ((hours-40)*otrate)
        return pay
    else:
        pay = hours * rate
        return pay
pay_number= float(pay(hours,rate))
print(pay_number)  
if pay_number < 300:
    print("Light week")
elif pay_number >= 300 and pay_number<=600:
    print("normal week")
else:
    print("Strong week")
    