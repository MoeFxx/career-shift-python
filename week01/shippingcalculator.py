def dev_fee(distance):
    if distance > 5:
        distance_change = distance - 5
        total_fee = fixed_fee + (distance_change * 8)
        return total_fee
    else:
        return fixed_fee
fixed_fee = 50
try:
    distance= int(input("distance : "))
except:
    print("Invalid input. Please enter a number.")
    exit()
    
print(dev_fee(distance))