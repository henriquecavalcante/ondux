import logging
import sys
from pprint import pprint

from learning.content_based import attribute_frequency, numeric_matching
from learning.knowledge_base import KnowledgeBase
from utils import functions as F
from utils import log_settings


def match_blocks(blocks_list, k_base):
    '''Associate each block generated in the Blocking step
    with an attribute represented in the knowledge base'''
    matched_blocks = []
    for blocks in blocks_list:
        labeled_blocks = []
        for block in blocks:
            labeled_blocks.append((block, classify_block(block, k_base)))
        matched_blocks.append(labeled_blocks)
    return matched_blocks

def classify_block(block, k_base):
    '''Classify a block based on content-based features
    extracted from Knowledge Base'''
    max_score = 0
    label = "none"
    attr_list = k_base.get_attributes()
    for attr in attr_list:
        if block.isdigit():
            score = numeric_matching(block, attr, k_base)
        else:
            score = attribute_frequency(block, attr, k_base)
        if score > max_score:
            max_score = score
            label = attr
    return label
