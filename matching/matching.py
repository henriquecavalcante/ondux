import logging
import sys
from pprint import pprint

from learning.content_based import attribute_frequency, numeric_matching
from learning.knowledge_base import KnowledgeBase
from utils import functions as F
from utils import log_settings


def match_blocks(blocks_list, k_base):
    '''Associate each block generated in the
    Blocking step with an attribute represented
    in the knowledge base'''
    matched_blocks = []
    for blocks in blocks_list:
        labeled_block = []
        for block in blocks:
            labeled_block.append((block, classify_block(block, k_base)))
        matched_blocks.append(labeled_block)
    return matched_blocks

def classify_block(block, k_base):
    max_score = 0
    label = "none"
    attr_list = k_base.get_attributes()
    for attr in attr_list:
        score = attribute_frequency(block, attr, k_base)
        if score > max_score:
            max_score = score
            label = attr
    return label
