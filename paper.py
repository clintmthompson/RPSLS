from choices import Choices


class Paper(Choices):

    def __init__(self):
        self.name = 'paper'
        self.beats = ['rock', 'spock']
        self.loses_to = ['scissors', 'lizard']
        super().__init__()
