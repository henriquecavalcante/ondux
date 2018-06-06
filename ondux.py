import logging
import sys
from pprint import pprint

from blocking.blocking import extract_blocks
from evaluation.results_evaluation import ResultsEvaluation as RE
from learning.knowledge_base import KnowledgeBase
from matching.matching import match_blocks
from reinforcement.psm import PSM
from reinforcement.reinforcement import reinforce
from utils import functions as F
from utils import log_settings

logger = log_settings.initialize_logs()


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

def run_reinforcement(matching_list, k_base):
    '''Reinforce Matching outcome taking into consideration
    structure-based features'''
    psm = PSM(matching_list, k_base)
    reinforce(matching_list, psm, k_base.get_attributes())

def run_evaluation(reference_file, results_file, attributes):
    '''Evaluate the results of the experiments'''
    RE.evaluate(reference_file, results_file, attributes)

def main(knowledge_base=None, input_file=None, reference_file=None):
    '''Run ONDUX extraction steps'''
    logger.info('Creating knowledge base...')
    k_base = create_k_base(knowledge_base)
    logger.info('Knowledge base created!')

    logger.info('Running blocking step over input file...')
    blocking_list = run_blocking(input_file, k_base)
    logger.info('Blocking step done!')

    logger.info('Running matching step over list of blocks...')
    matching_list = run_matching(blocking_list, k_base)
    logger.info('Matching step done!')

    logger.info('Running reinforcement step over matching list...')
    run_reinforcement(matching_list, k_base)
    logger.info('Reinforcement step done!')

    logger.info('Saving results...')
    F.save_results(matching_list)

    logger.info('Evaluating results...')
    run_evaluation(reference_file, 'results.xml', k_base.get_attributes())

if __name__ == "__main__":
    try:
        knowledge_base = sys.argv[1]
        input_file = sys.argv[2]
        reference_file = sys.argv[3]
    except IndexError as e:
        logger.error('Missing arguments. When running ondux you must '
        'pass as parameter the knowledge base and the input file.')
    finally:
        main(knowledge_base, input_file, reference_file)
