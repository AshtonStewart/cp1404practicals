#get user score as a float input. Could also be an int input as they should only be whole numbers
score = float(input("Enter score: "))
#Next few lines basically do the same thing, checking if the input is in a range then responds accordingly

if score >= 0 and score < 50:
    print("Bad")
elif score >= 50 and score < 90:
    print("Passable")
elif score >= 90  and score <= 100:
    print("Excellent")

else:
    print("invalid score")