import random
from rock import Rock
from paper import Paper
from scissors import Scissors
from lizard import Lizard
from spock import Spock


def run_game():
    play_rock = Rock()
    play_paper = Paper()
    play_scissors = Scissors()
    play_lizard = Lizard()
    play_spock = Spock()

    list_of_choices = [play_rock, play_paper, play_scissors, play_lizard, play_spock]

    def ai_turn():
        choice = list_of_choices[random.randint(0, 4)].name
        return choice

    def vs_computer():
        user_choice = input("Select from:\n0: Rock\n1: Paper\n2: Scissors\n3: Lizard\n4: Spock___")
        user_result = list_of_choices[int(user_choice)].name
        computer_result = ai_turn()
        print(user_result)
        print(computer_result)

    vs_computer()
