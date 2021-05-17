from choices import Choices


class Scissors(Choices):

    def __init__(self):
        self.name = 'Scissors'
        self.beats = ['Lizard', 'Paper']
        self.loses_to = ['Spock', 'Rock']
        super().__init__()
