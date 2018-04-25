class Occurrence:
    '''
    Represent the terms that occur in the Knowledge Base

    Occurrences have the following properties:
        term: A string representing the occurrence name.
        number: A counter representing the number of occurrences of a term.
    '''

    def __init__(self, term):
        self.term = term
        self.frequency = 1