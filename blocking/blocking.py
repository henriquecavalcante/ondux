import logging
from pprint import pprint

from blocking.block import Block
from utils import functions as F

logger = logging.getLogger(__name__)


def extract_blocks(input_file, k_base):
    '''Extract block structure for each value in input file'''
    r_input = [r for r in F.read_input(input_file)]
    normalized_input = [F.remove_stop_words(F.normalize_str(v))
                        for v in r_input]
    blocks = []
    for raw_terms, record in zip(r_input, normalized_input):
        blocks.append(build_blocks(record.split(), raw_terms.split(), k_base))
    return blocks


def build_blocks(terms, raw_terms, k_base):
    '''Build a set of blocks for a string'''
    blocks_list = []
    blocks_list.append(Block(terms[0], raw_terms[0]))
    i = 0
    j = 1
    while j < len(terms):
        if not co_occurs(terms[j-1], terms[j], k_base):
            blocks_list.append(Block('', ''))
            i += 1
        if blocks_list[i].value in '':
            blocks_list[i].value += terms[j]
            blocks_list[i].raw_value += raw_terms[j]
        else:
            blocks_list[i].value += ' ' + terms[j]
            blocks_list[i].raw_value += ' ' + raw_terms[j]
        j += 1
    return blocks_list


def co_occurs(current_term, next_term, k_base):
    '''Verify if the current term and next term are known
    to co-occur in some occurrence in the knowledge base'''
    if current_term in k_base.inverted_k_base and next_term in k_base.inverted_k_base:
        co_occurrences = k_base.co_occurrences[current_term]
        if next_term in [x[0] for x in co_occurrences]:
            return True
    return False
