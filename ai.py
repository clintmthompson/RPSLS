from player import Player


class Ai(Player):

    def __init__(self, ai_name):
        self.name = ai_name
        super().__init__()

