import logging
import os
import sys
from pprint import pprint

from learning.content_based import attribute_frequency
from learning.knowledge_base import KnowledgeBase


def create_k_base(kb):
    '''Create knowledge base from the input file'''
    return KnowledgeBase(kb)

def extract_content_based_features(k_base):
    '''Create knowledge base from the input file'''
    attribute_frequency('centro', 'bairro', k_base)

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
    k_base = create_k_base(knowledge_base)
    extract_content_based_features(k_base)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
