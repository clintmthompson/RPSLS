from choices import Choices


class Rock(Choices):

    def __init__(self):
        self.name = 'rock'
        self.beats = ['scissors', 'lizard']
        self.loses_to = ['paper', 'spock']
        super().__init__()




