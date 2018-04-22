import math
import os
import re
import sys
from pprint import pprint

from utils import functions as F

from .knowledge_base import KnowledgeBase


def attribute_frequency(canditate_value, attribute, k_base):
    '''Estimate the similarity between the content of a
    candidate value s and the values of an attribute A
    represented in the knowledge base.'''
    terms = canditate_value.split()
    sum_fitness = 0.0
    for term in terms:
        sum_fitness += fitness(term, attribute, k_base)
    return sum_fitness/len(terms)

def fitness(term, attribute, k_base):
    '''Evaluate how typical a term t is among the values
    of attribute A

    Properties:
        f_ta: number of distinct values of A that contain the term t
        f_max: highest frequency of any term among the values of A
        n_t: total number of occurrences of the term t in all attributes
    '''
    f_ta = k_base.get_term_frequency_by_attribute(term, attribute)
    if f_ta > 0:
        f_max = k_base.attribute_statistics[attribute].most_common_term_frequency
        n_t = k_base.get_term_occurrence_number(term)
        return (f_ta/n_t)*(f_ta/f_max)
    return 0.0

def numeric_matching(canditate_value, attribute, k_base):
    ''' Calculate the similarity between a numeric value present in a
    candidate value S and the set of values of an attribute A

    Properties:
        attr_avg: average of the values of an attribute A
        attr_stdev: standard deviation of the values of an attribute A
    '''
    attr_avg = k_base.attribute_statistics[attribute].average
    attr_stdev = k_base.attribute_statistics[attribute].standard_deviation
    return math.exp(-(math.pow((int(canditate_value) - attr_avg), 2.0)/(2 * math.pow(attr_stdev, 2.0))))
