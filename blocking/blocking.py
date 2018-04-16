import logging
import sys
from pprint import pprint

from utils import functions as F
from utils import log_settings


def extract_blocks(input_file, k_base):
    '''Extract block structure for each value in input file'''
    normalized_input = [F.normalize_str(v) for v in F.read_input(input_file)]
    blocks = []
    for value in normalized_input:
        temp = [v.strip() for v in build_blocks(value.split(), k_base) if v not in '']
        blocks.append(temp)
    return blocks

def build_blocks(terms, k_base):
    '''Build a set of blocks for a string'''
    blocks = ['']*len(terms)
    blocks[0] = terms[0]
    i = 0
    j = 1
    while j < len(terms):
        if not co_occurs(terms[j], terms[j-1], k_base):
            i += 1
        blocks[i] += ' ' + terms[j]
        j += 1
    return blocks

def co_occurs(current_term, previous_term, k_base):
    '''Verify if the current term and next term are known
    to co-occur in some occurrence in the knowledge base'''
    if current_term in k_base.inverted_k_base and previous_term in k_base.inverted_k_base:
        current_attr = k_base.inverted_k_base[current_term]
        previous_attr = k_base.inverted_k_base[previous_term]
        for c_attr in current_attr:
            for p_attr in previous_attr:
                if c_attr[0] == p_attr[0]:
                    return True
    return False
