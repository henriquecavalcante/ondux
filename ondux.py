import logging
import os
import sys

from utils import functions


def get_cb_features(knowledge_base):
    '''Get content-based features learned from knowledge
    base'''
    functions.parse_kb(knowledge_base)

def run_blocking():
    '''Segment input string in units called blocks'''
    pass

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
    get_cb_features(knowledge_base)
    # F.read_input(input_file)
    # run_blocking()
    # run_matching()
    # run_reinforcement()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
