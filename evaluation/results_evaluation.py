import logging
import re
import xml.etree.ElementTree as ET
from pprint import pprint

from evaluation.metrics import Metrics
from utils import functions as F

logger = logging.getLogger(__name__)

class ResultsEvaluation:
    '''Compute the evaluation metrics on the results of the experiments'''
    @staticmethod
    def evaluate(reference_file, results_file, attributes):
        '''Read reference and result files and then calculate evaluation metrics'''
        reference = F.read_input(reference_file)
        results = F.read_input(results_file)
        results_stats = {}
        reference_stats = {}
        right_answers = {}
        attr_evaluation = {}
        for attr in attributes:
            attr_evaluation[attr] = Metrics()

        for res, ref in zip(results, reference):
            result_record = ET.fromstring('<record>'+res+'</record>')
            reference_record = ET.fromstring('<record>'+ref+'</record>')

            for reference_block in reference_record:
                if reference_block.tag not in reference_stats:
                    reference_stats[reference_block.tag] = len(reference_block.text.split())
                else:
                    reference_stats[reference_block.tag] += len(reference_block.text.split())

            for result_block in result_record:
                if result_block.tag is not 'none' and result_block.tag not in results_stats:
                    results_stats[result_block.tag] = len(result_block.text.split())
                else:
                    results_stats[result_block.tag] += len(result_block.text.split())

            for result_block in result_record:
                for reference_block in reference_record:
                    if F.normalize_str(result_block.text) in F.normalize_str(reference_block.text) and result_block.tag == reference_block.tag:
                        if result_block.tag not in right_answers:
                            right_answers[result_block.tag] = len(result_block.text.split())
                        else:
                            right_answers[result_block.tag] += len(result_block.text.split())
                        break

        for attr in attributes:
            if attr in results_stats and attr in reference_stats and attr in right_answers:
                attr_evaluation[attr].precision = right_answers[attr] / results_stats[attr]
                attr_evaluation[attr].recall = right_answers[attr] / reference_stats[attr]
                attr_evaluation[attr].f_measure = (2*attr_evaluation[attr].precision*attr_evaluation[attr].recall)/(attr_evaluation[attr].precision+attr_evaluation[attr].recall)

        for attr in attr_evaluation:
            if attr_evaluation[attr].f_measure > 0:
                print(attr, '\tP: ', attr_evaluation[attr].precision, '\tR: ', attr_evaluation[attr].recall, '\tF: ', attr_evaluation[attr].f_measure)
