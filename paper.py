from choices import Choices


class Paper(Choices):

    def __init__(self):
        self.name = 'Paper'
        self.beats = ['Rock', 'Spock']
        self.loses_to = ['Scissors', 'Lizard']
        super().__init__()
