import random

values = ['rock', 'paper', 'scissors']
scores = {'WIN':0, 'TIE':0, 'LOSS':0}
counter = 1


class Hand:

    def __init__(self, value):
        self.value = value

    def challenge(self, hand):
        if hand.value == self.value:
            return "TIE"
        elif self.value == 'rock' and hand.value == 'paper':
            return "LOSS"
        elif self.value == 'scissors' and hand.value == 'rock':
            return "LOSS"
        elif self.value == 'paper' and hand.value == 'scissors':
            return "LOSS"
        else:
            return "WIN"


def get_computer_choice():
    return Hand(random.choice(values))


def get_user_choice():
    user_input = input("\n#" + str(counter) + " Enter your choice: rock, paper or scissors. (Exit to leave)\n").lower()
    while user_input not in values:
        if user_input == 'exit':
            print("Bye")
            exit()
        user_input = input("\n Invalid input\nEnter your choice: rock, paper och scissors \n")

    return Hand(user_input)


while True:

    computer_choice = get_computer_choice()
    player_choice = get_user_choice()

    result = player_choice.challenge(computer_choice)

    scores[result] = scores[result] + 1

    print(result + "! Computer chose " + computer_choice.value + "\nScores:" + str(scores))
    counter = counter + 1