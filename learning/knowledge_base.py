import logging
import re
import statistics
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pprint import pprint

from utils import functions as F
from utils import log_settings

from .inverted_index import InvertedIndex
from .occurrence import Occurrence

logger = log_settings.initialize_logs(__name__)

class KnowledgeBase:
    """A KnowledgeBase has the following properties:

    Attributes:
        k_base: A dict representing the attributes and their list of terms
        inverted_k_base: A dict representing the all terms of the Knowledge
        Base and the attributes they are present
    """

    def __init__(self, kb_file):
        """Return a Knowledge Base object"""
        self.k_base = {}
        self.init_kb(kb_file)
        self.inverted_k_base = InvertedIndex(self.k_base).inverted_k_base
        pprint(self.inverted_k_base)

    def init_kb(self, kb_file):
        '''Parse Knowledge Base and prepare it to extract
        the content-based features'''
        logger.debug('parsing knowlede base file')
        tree = ET.parse(kb_file)
        root = tree.getroot()
        for item in root:
            attribute = F.normalize_str(item.tag)
            value = F.remove_stop_words(F.normalize_str(item.text))

            for term in value:
                occurrence = Occurrence(term)

                if attribute in self.k_base:
                    if term not in [obj.term for obj in self.k_base[attribute]]:
                        self.k_base[attribute].append(occurrence)
                    else:
                        occ = [v for v in self.k_base[attribute] if v.term == term]
                        occ[0].number += 1
                else:
                    self.k_base[attribute] = [occurrence]

    def get_most_common_term_by_attribute(self, attr):
        '''Get the highest frequency of any term among the values of A'''
        terms = [v for v in self.k_base[attr]]
        return max(x.number for x in terms if x.term)

    def get_term_frequency_by_attribute(self, term, attr):
        '''Get the number of distinct values of attribute A that contain the term t'''
        terms = [v for v in self.k_base[attr] if v.term == term]
        return terms[0].number

    def get_term_occurrence_number(self, term):
        '''Get the total number of occurrences of the term t in all attributes'''
        occ = 0
        if term in self.inverted_k_base:
            for freq in self.inverted_k_base[term]:
                occ += freq[1]
            return occ
        return 0

    def get_values_average(self, attribute):
        '''Get the average of numeric values of an attribute A'''
        numeric_values = [int(v.term) for v in self.k_base[attribute] if re.match(r'^\d+$', v.term)]
        pprint(numeric_values)
        return statistics.mean(numeric_values)

    def get_values_standard_deviation(self, attribute):
        '''Get the standard deviation of numeric values of an attribute A'''
        numeric_values = [int(v.term) for v in self.k_base[attribute] if re.match(r'^\d+$', v.term)]
        return statistics.stdev(numeric_values)
