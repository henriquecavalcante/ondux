import logging

logger = logging.getLogger(__name__)

class StructureBasedFeatures:
    '''
    Represent the structure based features that can be
    extracted from the Knowledge Base.

    StructureBasedFeatures has the following structure-based similarity functions:
        sequencing: based on the terms transitions.
        positioning: based on the terms positions.
    '''