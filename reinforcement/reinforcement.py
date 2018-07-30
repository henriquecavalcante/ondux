import logging
from pprint import pprint
from utils import functions as F
import operator

logger = logging.getLogger(__name__)


def reinforce(matching_list, psm, attribute_list):
    '''Revise the pre-labeling made by the Matching step over the blocks.
    Unmatched blocks are labeled and mismatched blocks are expected to be
    correctly re-labeled.'''
    attribute_index = init_attrbute_index(attribute_list)

    for record in matching_list:
        i = 0
        while i < len(record):
            attribute_score = init_attribute_score(attribute_list)
            current_block = record[i]
            if current_block.label is not 'none':
                for attr in attribute_list:
                    t_score = psm.t_matrix[attribute_index[current_block.label]
                                           ][attribute_index[attr]]
                    p_score = psm.p_matrix[attribute_index[attr]][i+1]
                    attribute_score[attr] = (
                        1 - ((1 - current_block.matching_score[attr])*(1 - t_score)*(1 - p_score)))
                # current_block.reinforcement_score = attribute_score
                # current_block.label = current_block.get_top_reinforcement_score()
            else:
                if i > 0:
                    previous_block = record[i-1]
                    for attr in attribute_list:
                        t_score = psm.t_matrix[attribute_index[previous_block.label]
                                               ][attribute_index[attr]]
                        p_score = psm.p_matrix[attribute_index[attr]][i+1]
                        attribute_score[attr] = (
                            1 - ((1 - previous_block.matching_score[attr])*(1 - t_score)*(1 - p_score)))
                    current_block.reinforcement_score = attribute_score
                    current_block.label = current_block.get_top_reinforcement_score()
                else:
                    for attr in attribute_list:
                        p_score = psm.p_matrix[attribute_index[attr]][1]
                        attribute_score[attr] = (
                            1 - ((1 - current_block.matching_score[attr])*(1 - p_score)))
                    current_block.reinforcement_score = attribute_score
                    current_block.label = current_block.get_top_reinforcement_score()
            i += 1


def init_attribute_score(attribute_list):
    attribute_score = {}
    for attr in attribute_list:
        attribute_score[attr] = 0
    return attribute_score


def init_attrbute_index(attribute_list):
    attribute_index = {}
    for i, attr in enumerate(attribute_list):
        attribute_index[attr] = i + 1
    return attribute_index
