import logging
import re
import statistics
from pprint import pprint

from utils import functions as F

from .attribute import Attribute
from .inverted_index import InvertedIndex
from .occurrence import Occurrence

logger = logging.getLogger(__name__)


class KnowledgeBase:
    """A KnowledgeBase has the following properties:

    Attributes:
        k_base: A dict representing the attributes and their list of terms.
        inverted_k_base: A dict representing the all terms of the Knowledge Base and
        the attributes they are present.
        attribute_statistics: A dict representing each attribute statistics.
    """

    def __init__(self, kb_file):
        """Return a Knowledge Base object"""
        self.k_base = {}
        self.inverted_k_base = {}
        self.co_occurrences = {}
        self.attribute_statistics = {}
        self.init_kb(kb_file)
        self.init_inverted_k_base()
        self.init_atribute_statistics()

    def init_kb(self, kb_file):
        '''Parse Knowledge Base and prepare it to extract the content-based features'''
        logger.info('Parsing knowledge base file...')
        data = F.read_k_base(kb_file)

        for item in data:
            attribute = item.tag
            value = F.remove_stop_words(F.normalize_str(item.text))

            # Check if a value contains only stop words
            if not value:
                continue

            terms = value.split()
            i = 0
            while i < len(terms)-1:
                if terms[i] in self.co_occurrences:
                    if (terms[i+1],attribute) not in self.co_occurrences[terms[i]]:
                        self.co_occurrences[terms[i]].append((terms[i+1], attribute))
                else:
                    self.co_occurrences[terms[i]] = []
                i += 1
            if terms[-1] not in self.co_occurrences:
                self.co_occurrences[terms[-1]] = []

            for term in terms:
                occurrence = Occurrence(term)
                if attribute in self.k_base:
                    if term not in [obj.term for obj in self.k_base[attribute]]:
                        self.k_base[attribute].append(occurrence)
                    else:
                        occ = [v for v in self.k_base[attribute] if v.term == term]
                        occ[0].frequency += 1
                else:
                    self.k_base[attribute] = [occurrence]

    def init_inverted_k_base(self):
        '''Create an inverted index for the Knowledge Base'''
        self.inverted_k_base = InvertedIndex(self.k_base).inverted_k_base

    def get_attributes(self):
        '''Get a list with all attributes in the Knowledge Base'''
        return [v for v in self.k_base.keys()]

    def init_atribute_statistics(self):
        '''Set a list of attribute statistics'''
        for attr in self.get_attributes():
            most_commom = self.get_most_common_term_by_attribute(attr)
            avg = 0.0
            stdev = 0.0
            numeric_values = [int(v.term) for v in self.k_base[attr] if re.match(r'^\d+$', v.term)]
            if len(numeric_values):
                avg = statistics.mean(numeric_values)
            if len(numeric_values) > 1:
                stdev = statistics.stdev(numeric_values)
            self.attribute_statistics[attr] = Attribute(attr, avg, stdev, most_commom)

    def get_most_common_term_by_attribute(self, attr):
        '''Get the highest frequency of any term among the values of A'''
        terms = [v for v in self.k_base[attr]]
        return max(x.frequency for x in terms if x.term)

    def get_term_frequency_by_attribute(self, term, attr):
        '''Get the number of distinct values of attribute A that contain the term t'''
        if term in self.inverted_k_base:
            frequency = [v[1] for v in self.inverted_k_base[term] if v[0] == attr]
            if len(frequency):
                return frequency[0]
        return 0

    def get_term_occurrence_number(self, term):
        '''Get the total number of occurrences of the term t in all attributes'''
        if term in self.inverted_k_base:
            return sum(v[1] for v in self.inverted_k_base[term])
        return 0
