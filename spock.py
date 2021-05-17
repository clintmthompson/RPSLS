from choices import Choices


class Spock(Choices):

    def __init__(self):
        self.name = 'Spock'
        self.beats = ['Rock', 'Scissors']
        self.loses_to = ['Lizard', 'Paper']
        super().__init__()
