from game_data import data
from art import logo, vs
import random
from log import compare
print("Welcome to Higher or Lower")

print(logo)

wins = 0

def set_dict(a, b):
    return {
        "A": a,
        "B": b
    }

def set_option ():
    return data.pop(random.randint(0, len(data) - 1))

option_a = set_option()
option_b = set_option()
user_dict = set_dict(option_a, option_b)
opponent_dict = set_dict(option_b, option_a)

# Log options to the screen
valid_answers = True
while valid_answers:
    compare("A", option_a['name'], option_a['description'], option_a['country'])
    print(vs)
    compare("B", option_b['name'], option_b['description'], option_b['country'])
    answer = input("Who has more followers? Type 'A' or 'B': ")
    while not answer == 'A' and not answer == 'B':
        answer = input("Sorry! I don't recognize that option. Guess again? Type 'A' or 'B': ")

    if user_dict[answer]["follower_count"] > opponent_dict[answer]["follower_count"]:
        wins += 1
        print(f"Correct! You have {wins} points!")

        if user_dict[answer] == option_a:
            option_b = set_option()
        else:
            option_a = set_option()

        user_dict = set_dict(option_a, option_b)
        opponent_dict = set_dict(option_b, option_a)
    else:
        valid_answers = False

print(f"You finished with a score of {wins}!")