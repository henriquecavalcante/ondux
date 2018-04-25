class Attribute:
    '''
    Represent the attribute that occur in the Knowledge Base

    Attributes have the following properties:
        name: A string representing the attribute name.
        mean: A number representing the mean of the numeric
        values.
        standard_deviation: A number representing the standard
        deviation of the numeric values.
        most_common_term_frequency: A number representing the
        frenquency of the most commom term among the attribute
        occurrences.
    '''

    def __init__(self, name, avg, stdev, freq):
        self.name = name
        self.average = avg
        self.standard_deviation = stdev
        self.most_common_term_frequency = freq
