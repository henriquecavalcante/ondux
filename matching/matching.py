import logging
from pprint import pprint

from learning.knowledge_base import KnowledgeBase
from utils import functions as F

from .content_based import ContentBasedFeatures as CBF

logger = logging.getLogger(__name__)

def match_blocks(blocking_list, k_base):
    '''Associate each block generated in the Blocking step
    with an attribute represented in the knowledge base'''
    matching_blocks = []
    for blocks in blocking_list:
        labeled_blocks = []
        for block in blocks:
            labeled_blocks.append(classify_block(block, k_base))
        matching_blocks.append(labeled_blocks)
    return matching_blocks

def classify_block(block, k_base):
    '''Classify a block based on content-based features
    extracted from Knowledge Base'''
    max_score = 0
    label = "none"
    attr_list = k_base.get_attributes()
    for attr in attr_list:
        if block.value.isdigit():
            score = CBF.numeric_matching(block.value, attr, k_base)
        else:
            score = CBF.attribute_frequency(block.value, attr, k_base)
        if score > max_score:
            max_score = score
            label = attr
    block.matching_score = max_score
    block.label = label
    return block
