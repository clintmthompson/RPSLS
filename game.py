import random
from rock import Rock
from paper import Paper
from scissors import Scissors
from lizard import Lizard
from spock import Spock
from human import Human
from ai import Ai


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
        player_one = Human("Player One")
        player_two = Ai("Player Two")
        while player_one.points < 3 and player_two.points < 3:
            user_choice = input("Select from:\n0: Rock\n1: Paper\n2: Scissors\n3: Lizard\n4: Spock\n________________________________")
            while user_choice != '0' and user_choice != '1' and user_choice != '2' and user_choice != '3' and user_choice != '4':
                print('invalid choice')
                user_choice = input("try again")
            user_result = list_of_choices[int(user_choice)]
            computer_result = ai_turn()
            print(f'Player One: {user_result.name}')
            print(f'Player Two: {computer_result}')
            if user_result.beats[0] == computer_result or user_result.beats[1] == computer_result:
                print('Player one wins the round')
                player_one.points += 1
                print(f'{player_one.points} - {player_two.points}')
                print('________________________________')
                print('________________________________\n\n\n\n\n')
            elif user_result.loses_to[0] == computer_result or user_result.loses_to[1] == computer_result:
                print('Player two wins the round')
                player_two.points += 1
                print(f'{player_one.points} - {player_two.points}')
                print('________________________________')
                print('________________________________\n\n\n\n\n')
            elif user_result.name == computer_result:
                print("It's a tie, how boring")
                print(f'{player_one.points} - {player_two.points}')
                print('________________________________')
                print('________________________________\n\n\n\n\n')
            else:
                print('invalid input1')
            if player_one.points == 3:
                print('PLAYER ONE IS VICTORIOUS')
            elif player_two.points == 3:
                print('PLAYER TWO IS VICTORIOUS')

    def vs_player():
        player_one = Human("Player One")
        player_two = Human("Player Two")
        while player_one.points < 3 and player_two.points < 3:
            user_choice_one = input("Select from:\n0: Rock\n1: Paper\n2: Scissors\n3: Lizard\n4: Spock\nPlayer one input your choice")
            while user_choice_one != '0' and user_choice_one != '1' and user_choice_one != '2' and user_choice_one != '3' and user_choice_one != '4':
                print('invalid choice')
                user_choice_one = input("try again")
            user_result_one = list_of_choices[int(user_choice_one)]
            user_choice_two = input("Player Two Input your choice\n________________________________")
            while user_choice_two != '0' and user_choice_two != '1' and user_choice_two != '2' and user_choice_two != '3' and user_choice_two != '4':
                print('invalid choice')
                user_choice_two = input("try again")
            user_result_two = list_of_choices[int(user_choice_two)]
            print(f'Player One: {user_result_one.name}')
            print(f'Player Two: {user_result_two.name}')
            if user_result_one.beats[0] == user_result_two.name or user_result_one.beats[1] == user_result_two.name:
                print('Player one wins the round')
                player_one.points += 1
                print(f'{player_one.points} - {player_two.points}')
                print('________________________________')
                print('________________________________\n\n\n\n\n')
            elif user_result_one.loses_to[0] == user_result_two.name or user_result_one.loses_to[1] == user_result_two.name:
                print('Player two wins the round')
                player_two.points += 1
                print(f'{player_one.points} - {player_two.points}')
                print('________________________________')
                print('________________________________\n\n\n\n\n')
            elif user_result_one.name == user_result_two.name:
                print("It's a tie, how boring")
                print(f'{player_one.points} - {player_two.points}')
                print('________________________________')
                print('________________________________\n\n\n\n\n')
            if player_one.points == 3:
                print('PLAYER ONE IS VICTORIOUS')
            elif player_two.points == 3:
                print('PLAYER TWO IS VICTORIOUS')

    player_select = input('1 or 2 players? (type 1 or 2)')
    if int(player_select) == 1:
        vs_computer()
    elif int(player_select) == 2:
        vs_player()
