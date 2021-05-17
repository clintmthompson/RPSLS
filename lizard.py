from choices import Choices


class Lizard(Choices):

    def __init__(self):
        self.name = 'lizard'
        self.beats = ['spock', 'paper']
        self.lose_to = ['rock', 'scissors']
        super().__init__()
