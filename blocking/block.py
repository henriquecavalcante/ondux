class Block:
    '''
    Represent each block genarated during blocking step

    Attributes have the following properties:
        value: A string representing the block value.
        raw_value: A string representing the raw input value.
        label: A string representing the block label.
        matching_score: A number representing the highest
        score got in matching step.
        reinforcement_score: A number representing the highest
        score got in reinforcement step.
    '''

    def __init__(self, value, raw):
        self.value = value
        self.raw_value = raw
        self.label = ''
        self.matching_score = 0
        self.reinforcement_score = 0