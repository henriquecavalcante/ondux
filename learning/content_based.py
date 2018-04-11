import math
import os
import sys
from collections import Counter
from pprint import pprint

from utils import functions as F

from .knowledge_base import KnowledgeBase


def attribute_frequency(canditate_value, attribute, k_base):
    '''Estimate the similarity between the content of a
    candidate value s and the values of an attribute A
    represented in the knowledge base.'''
    terms = canditate_value.split()
    for term in terms:
        fitness(F.normalize_str(term), attribute, k_base)

def fitness(term, attribute, k_base):
    '''Evaluate how typical a term t is among the values
    of attribute A

    Properties:
        f_ta: number of distinct values of A that contain the term t
        f_max: highest frequency of any term among the values of A
        n_t: total number of occurrences of the term t in all attributes
    '''
    f_ta = k_base.get_term_frequency_by_attribute(term, attribute)
    f_max = k_base.get_most_common_term_by_attribute(attribute)
    n_t = k_base.get_term_occurrence_number(term)

    return (f_ta/n_t)*(f_ta/f_max[1])

def numeric_matching(canditate_value, attribute, k_base):
    ''' Calculate the similarity between a numeric value present in a
    candidate value S and the set of values of an attribute A

    Properties:
        attr_avg: average of the values of an attribute A
        attr_stdev: standard deviation of the values of an attribute A
    '''
    attr_avg = k_base.get_values_average(attribute)
    attr_stdev = k_base.get_values_standard_deviation(attribute)
    print(math.exp((canditate_value - attr_avg)/(2 * math.pow(attr_stdev, 2.0))))
