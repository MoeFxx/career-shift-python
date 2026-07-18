score = input("Enter your score (0-100): ")
try:
    score = int(score) 
except: 
    print("Invalid input. Please enter a number between 0 and 100.")
    exit()

if score <= 0 or score > 100:
    print("Invalid input. Please enter a number between 0 and 100.")

    exit()
if score >= 90: 
    print("Excellent!")
elif score >= 70 and score <= 89:
    print("Good")
elif score >=50 and score <= 69:
    print("Pass")
else:
    print("Need work")

if score >= 50:
    print("Congratulations! You passed the course.")
else:
    print("Sorry, you did not pass the course. Better luck next time.")