import logging
import math

logger = logging.getLogger(__name__)

class ContentBasedFeatures:
    '''
    Represent the content based features that can be
    extracted from the Knowledge Base.

    ContentBasedFeatures has the following content-based similarity functions:
        attribute_frequency: used for textual values.
        numeric_matching: used for numeric values.
    '''

    @staticmethod
    def attribute_frequency(canditate_value, attribute, k_base):
        '''Estimate the similarity between the content of a
        candidate value s and the values of an attribute A
        represented in the knowledge base.'''
        terms = canditate_value.split()
        sum_fitness = 0
        for term in terms:
            sum_fitness += ContentBasedFeatures.fitness(term, attribute, k_base)
        try:
            return sum_fitness/len(terms)
        except ZeroDivisionError:
            return 0

    @staticmethod
    def fitness(term, attribute, k_base):
        '''Evaluate how typical a term t is among the values
        of attribute A.

        Properties:
            f_ta: number of distinct values of A that contain the term t.
            f_max: highest frequency of any term among the values of A.
            n_t: total number of occurrences of the term t in all attributes.
        '''
        f_ta = k_base.get_term_frequency_by_attribute(term, attribute)
        f_max = k_base.attribute_statistics[attribute].most_common_term_frequency
        n_t = k_base.get_term_occurrence_number(term)
        try:
            return (f_ta/n_t)*(f_ta/f_max)
        except ZeroDivisionError:
            return 0

    @staticmethod
    def numeric_matching(canditate_value, attribute, k_base):
        ''' Calculate the similarity between a numeric value present in a
        candidate value S and the set of values of an attribute A.

        Properties:
            attr_avg: average of the values of an attribute A.
            attr_stdev: standard deviation of the values of an attribute A.
        '''
        attr_avg = k_base.attribute_statistics[attribute].average
        attr_stdev = k_base.attribute_statistics[attribute].standard_deviation
        try:
            return math.exp(-(math.pow((int(canditate_value) - attr_avg), 2.0)/(2 * math.pow(attr_stdev, 2.0))))
        except ZeroDivisionError:
            return 0
