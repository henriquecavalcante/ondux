import logging
import os
import sys
from pprint import pprint

from blocking.blocking import extract_blocks
from learning.content_based import attribute_frequency, numeric_matching
from learning.knowledge_base import KnowledgeBase
from utils import log_settings

logger = log_settings.initialize_logs(__name__)

def create_k_base(kb):
    '''Create knowledge base from the input file'''
    return KnowledgeBase(kb)

def extract_content_based_features(k_base):
    '''Create knowledge base from the input file'''
    print(attribute_frequency('regent square', 'neighborhood', k_base))
    print(numeric_matching(1921092, 'phone', k_base))

def run_blocking(input_file, k_base):
    '''Segment input file in units called blocks'''
    pprint(extract_blocks(input_file, k_base))

def run_matching():
    '''Associate blocks to labels using content-based
    features learned from KB'''
    pass

def run_reinforcement():
    '''Reinforce Matching outcome taking into consideration
    structure-based features'''
    pass

def main(knowledge_base=None, input_file=None):
    '''Run ONDUX extraction steps'''
    logger.info('creating knowledge base')
    k_base = create_k_base(knowledge_base)

    # logger.info('extracting content-based features from knowledge base')
    # extract_content_based_features(k_base)

    logger.info('running blocking step over input file')
    run_blocking(input_file, k_base)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
