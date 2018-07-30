class Metrics:
    '''
    Represent the metrics used for experimental evaluation

    Metrics have the following properties:
        precision: A number representing the precision.
        recall: A number representing the recall.
        f_measure: A number representing the f_measure.
    '''

    def __init__(self):
        self.precision = 0
        self.recall = 0
        self.f_measure = 0
