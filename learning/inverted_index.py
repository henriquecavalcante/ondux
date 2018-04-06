import sys
from collections import defaultdict


class InvertedIndex:
    """A InvertedIndex has the following properties:

    Attributes:
        inverted_k_base: A dict representing the all
        terms of the Knowledge Base and the attributes
        they are present
    """

    def __init__(self, k_base):
        """Return a Knowledge Base object"""
        self.inverted_k_base = defaultdict(list)
        self.create_inverted_k_base(k_base)

    def create_inverted_k_base(self, k_base):
        '''Create an inverted dict from the Knowledge Base'''
        for attribute in k_base:
            for occ in k_base[attribute]:
                self.inverted_k_base.setdefault(occ.term, []).append(attribute)
