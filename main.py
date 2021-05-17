import random
from rock import Rock
from paper import Paper
from scissors import Scissors
from lizard import Lizard
from spock import Spock


if __name__ == '__main__':
    play_rock = Rock()
    play_paper = Paper()
    play_scissors = Scissors()
    play_lizard = Lizard()
    play_spock = Spock()


def ai_turn():
    ai_choices = [play_rock, play_paper, play_scissors, play_lizard, play_spock]
    choice = ai_choices[random.randint(0, 4)].name
    return choice


print(ai_turn())




