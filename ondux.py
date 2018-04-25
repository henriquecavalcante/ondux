import logging
import os
import sys
from pprint import pprint

from blocking.blocking import extract_blocks
from learning.knowledge_base import KnowledgeBase
from matching.matching import match_blocks
from utils import log_settings

logger = log_settings.initialize_logs(__name__)

def create_k_base(kb):
    '''Create knowledge base from the input file'''
    return KnowledgeBase(kb)

def run_blocking(input_file, k_base):
    '''Segment input file in units called blocks'''
    return extract_blocks(input_file, k_base)

def run_matching(blocks_list, k_base):
    '''Associate blocks to labels using content-based
    features learned from KB'''
    return match_blocks(blocks_list, k_base)

def run_reinforcement():
    '''Reinforce Matching outcome taking into consideration
    structure-based features'''
    pass

def main(knowledge_base=None, input_file=None):
    '''Run ONDUX extraction steps'''
    logger.info('Creating knowledge base...')
    k_base = create_k_base(knowledge_base)
    logger.info('Knowledge base created!')

    logger.info('Running blocking step over input file...')
    blocks_list = run_blocking(input_file, k_base)
    logger.info('Blocking step done!')

    logger.info('Running matching step over list of blocks...')
    matching_list = run_matching(blocks_list, k_base)
    logger.info('Matching step done!')

    pprint(matching_list)

if __name__ == "__main__":
    try:
        main(sys.argv[1], sys.argv[2])
    except IndexError as e:
        logger.error('Missing arguments. When running ondux you must '
        'pass as parameter the knowledge base and the input file.')
