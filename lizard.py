from choices import Choices


class Lizard(Choices):

    def __init__(self):
        self.name = 'Lizard'
        self.beats = ['Spock', 'Paper']
        self.lose_to = ['Rock', 'Scissors']
        super().__init__()
