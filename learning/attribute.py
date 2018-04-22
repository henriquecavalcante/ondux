class Attribute:
    '''
    Represent the attribute that occur in the Knowledge Base

    Attributes have the following properties:
        name: A string representing the occurrence name.
        mean: A counter representing the number of occurrences of a term.
        standard_deviation
    '''

    def __init__(self, name, avg, stdev, freq):
        self.name = name
        self.average = avg
        self.standard_deviation = stdev
        self.most_common_term_frequency = freq
