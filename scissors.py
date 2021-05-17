from choices import Choices


class Scissors(Choices):

    def __init__(self):
        self.name = 'scissors'
        self.beats = ['lizard', 'paper']
        self.loses_to = ['spock', 'rock']
        super().__init__()
