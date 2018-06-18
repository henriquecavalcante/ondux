import operator


class Block:
    '''
    Represent each block genarated during blocking step

    Attributes have the following properties:
        value: A string representing the block value.
        raw_value: A string representing the raw input value.
        label: A string representing the block label.
        matching_score: A dict representing the score got from
        the content based features for each attribute.
        reinforcement_score: A dict representing the score got
        from the content based combined with sctructure based
        features for each attribute.
    '''

    def __init__(self, value, raw):
        self.value = value
        self.raw_value = raw
        self.label = ''
        self.matching_score = {}
        self.reinforcement_score = {}

    def get_top_matching_score(self):
        '''Return the label that has the max score on the matching step'''
        return max(self.matching_score.items(), key=operator.itemgetter(1))[0]

    def get_top_reinforcement_score(self):
        '''Return the label that has the max score on the reinforcement step'''
        return max(self.reinforcement_score.items(), key=operator.itemgetter(1))[0]
