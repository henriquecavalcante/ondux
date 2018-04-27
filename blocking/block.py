class Block:
    '''
    Represent each block genarated during blocking step

    Attributes have the following properties:
        value: A string representing the bloble value.
        label: A string representing the block label.
        matching_score: A number representing the highest
        score got in matching step.
        reinforcement_score: A number representing the highest
        score got in reinforcement step.
    '''

    def __init__(self, value):
        self.value = value
        self.label = ''
        self.matching_score = 0
        self.reinforcement_score = 0