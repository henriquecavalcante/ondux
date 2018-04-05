import sys
import xml.etree.ElementTree as ET

from .occurrence import Occurrence
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
                if term not in [obj.term for obj in self.base[attribute]]:
                    self.base[attribute].append(occurrence)
                else:
                    occ = [v for v in self.base[attribute] if v.term == term]
                    occ[0].number += 1
            else:
                self.base[attribute] = [occurrence]
