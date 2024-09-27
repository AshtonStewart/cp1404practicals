"""cp1404 Ashton Stewart
Program to get a score from the user and categorize it along with a random score
"""
import random

def main():
    score_num = int(input("What is your score?"))
    print(F"Your score of {score_num}" + " was " + score_categorizer(score_num))
    random_score = random.randint(0, 100)
    print(F"your random score of {random_score}" + " was " + score_categorizer(random_score))

def score_categorizer(score):
    if score > 100 or score < 0:
        return "invalid"
    elif score >= 90:
        return "excellent"
    elif score >= 50:
        return "good"
    else:
        return "bad"

main()