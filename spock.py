from choices import Choices


class Spock(Choices):

    def __init__(self):
        self.name = 'spock'
        self.beats = ['rock', 'scissors']
        self.loses_to = ['lizard', 'paper']
        super().__init__()
