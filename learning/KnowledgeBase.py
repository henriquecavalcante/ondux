import sys
import xml.etree.ElementTree as ET

from .Occurrence import Occurrence
from utils import functions as F


class KnowledgeBase:
    """A KnowledgeBase has the following properties:

    Attributes:
        base: A dict representing the attributes and their list of terms
    """

    def __init__(self, kb_file):
        """Return a Knowledge Base object"""
        self.base = {}
        self.parse_kb(kb_file)

    def parse_kb(self, kb_file):
        '''Parse Knowledge Base and prepare it to extract
        the content-based features'''
        tree = ET.parse(kb_file)
        root = tree.getroot()
        for item in root:
            attribute = F.clear_string(item.tag)
            term = F.clear_string(item.text)
            occurrence = Occurrence(term)

            if attribute in self.base:
                has_term = False
                term_index = -1
                temp = self.base[attribute]
                for index, obj in enumerate(temp):
                    if term in obj.term:
                        has_term = True
                        term_index = index

                if has_term:
                    self.base[attribute][term_index].number += 1
                else:
                    self.base[attribute].append(occurrence)
            else:
                self.base[attribute] = [occurrence]
