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
        player_one_points = 0
        player_two_points = 0
        while player_one_points < 3 and player_two_points < 3:
            user_choice = input("Select from:\n0: Rock\n1: Paper\n2: Scissors\n3: Lizard\n4: Spock\n________________________________")
            user_result = list_of_choices[int(user_choice)]
            computer_result = ai_turn()
            print(f'Player One: {user_result.name}')
            print(f'Player One: {computer_result}')
            if user_result.beats[0] == computer_result or user_result.beats[1] == computer_result:
                print('Player one wins the round')
                player_one_points += 1
                print(f'{player_one_points} - {player_two_points}')
                print('________________________________')
                print('________________________________')
            elif user_result.loses_to[0] == computer_result or user_result.loses_to[1] == computer_result:
                print('Player two wins the round')
                player_two_points += 1
                print(f'{player_one_points} - {player_two_points}')
                print('________________________________')
                print('________________________________')
            elif user_result.name == computer_result:
                print("It's a tie, how boring")
                print(f'{player_one_points} - {player_two_points}')
                print('________________________________')
                print('________________________________')
            if player_one_points == 3:
                print('PLAYER ONE IS VICTORIOUS')
            elif player_two_points == 3:
                print('PLAYER TWO IS VICTORIOUS')



    vs_computer()
