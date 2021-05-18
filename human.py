from player import Player


class Human(Player):

    def __init__(self, player_name):
        self.name = player_name
        super().__init__()
