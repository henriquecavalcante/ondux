import logging
from pprint import pprint
from utils import functions as F

logger = logging.getLogger(__name__)


def reinforce(matching_list, psm, attribute_list):
    '''Revise the pre-labeling made by the Matching step over the blocks.
    Unmatched blocks are labeled and mismatched blocks are expected to be
    correctly re-labeled.'''
    # TEMP
    sum_t_matrix(psm.t_matrix)

    attribute_index = {}
    for i, attr in enumerate(attribute_list):
        attribute_index[attr] = i + 1

    blocking_list = [b for b in matching_list]
    for blocks in blocking_list:
        compute_reinforment_score(blocks, psm, attribute_index)

    for attribute in attribute_list:
        for blocks in blocking_list:
            for block in blocks:
                if block.label in attribute:
                    score = 1 - ((1 - block.matching_score) * (1 - block.reinforcement_score))
                    # print(block.value + ' | ' + block.label + ' | ' + repr(block.matching_score) + ' | ' + repr(block.reinforcement_score) + ' | ' + repr(score))


def compute_reinforment_score(blocks, psm, attribute_index):
    '''Compute reinforment score for each block based on PSM probabilities'''
    for i in range(len(blocks)-1):
        current_block = blocks[i]
        next_block = blocks[i+1]
        if current_block.label is 'none' or next_block.label is 'none':
            continue
        current_block.reinforcement_score = psm.t_matrix[attribute_index[current_block.label]][attribute_index[next_block.label]]


def sum_t_matrix(t_matrix):
    # TEMP
    # print('\n----- MATRIX OF TRANSITIONS -----')
    # F.print_matrix(t_matrix)
    s = {}

    for i in range(len(t_matrix)-1):
        s[t_matrix[0][i+1]] = 0

    for i in range(len(t_matrix)):
        for j in range(len(t_matrix)):
            if i > 0 and j > 0:
                s[t_matrix[0][i]] += t_matrix[i][j]
    # TEMP
    # print('\n----- SUM OF TRANSITIONS FOR EACH ATTRIBUTE -----')
    # pprint(s)