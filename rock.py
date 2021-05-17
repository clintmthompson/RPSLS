from choices import Choices


class Rock(Choices):

    def __init__(self):
        self.name = 'Rock'
        self.beats = ['Scissors', 'Lizard']
        self.loses_to = ['Paper', 'Spock']
        super().__init__()




