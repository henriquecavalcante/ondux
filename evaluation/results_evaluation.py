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
        ResultsEvaluation.attribute_evaluation(reference_file, results_file, attributes)
        ResultsEvaluation.record_evaluation(reference_file, results_file, attributes)

    @staticmethod
    def attribute_evaluation(reference_file, results_file, attributes):
        '''Compute evaluation metrics per Attribute'''
        step = 'Matching Step' if results_file in 'matching_results.xml' else 'Reinforcement Step'
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

        print('----------------------------------------------------------------------------')
        print('{0} - Results Evaluation Per Attribute'.format(step))
        print('----------------------------------------------------------------------------')
        print('{:<15} {:<20} {:<20} {:<18}'.format('Attribute', 'Precision', 'Recall', 'F-Measure'))
        for k, v in attr_evaluation.items():
            if v.f_measure > 0:
                print('{:<15} {:<20} {:<20} {:<18}'.format(k, v.precision, v.recall, v.f_measure))

    @staticmethod
    def record_evaluation(reference_file, results_file, attributes):
        '''Compute evaluation metrics per Record'''
        step = 'Matching Step' if results_file in 'matching_results.xml' else 'Reinforcement Step'
        reference = F.read_input(reference_file)
        results = F.read_input(results_file)
        record_evaluation = []
        for res, ref in zip(results, reference):
            results_stats = {}
            reference_stats = {}
            right_answers = {}
            attr_evaluation = {}

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
                    attr_evaluation[attr] = Metrics()
                    attr_evaluation[attr].precision = right_answers[attr] / results_stats[attr]
                    attr_evaluation[attr].recall = right_answers[attr] / reference_stats[attr]
                    attr_evaluation[attr].f_measure = (2*attr_evaluation[attr].precision*attr_evaluation[attr].recall)/(attr_evaluation[attr].precision+attr_evaluation[attr].recall)
                elif attr in results_stats and attr not in reference_stats:
                    attr_evaluation[attr] = Metrics()

            record = Metrics()
            for attr in attr_evaluation:
                record.precision += attr_evaluation[attr].precision
                record.recall += attr_evaluation[attr].recall
                record.f_measure += attr_evaluation[attr].f_measure
            record.precision /= len(attr_evaluation)
            record.recall /= len(attr_evaluation)
            record.f_measure /= len(attr_evaluation)
            record_evaluation.append(record)

        precision = 0
        recall = 0
        f_measure = 0
        for record in record_evaluation:
            precision += record.precision
            recall += record.recall
            f_measure += record.f_measure
        precision /= len(results)
        recall /= len(results)
        f_measure /= len(results)

        print('----------------------------------------------------------------------------')
        print('{0} - Results Evaluation Per Record'.format(step))
        print('----------------------------------------------------------------------------')
        print('{:<20} {:<20} {:<18}'.format('Precision', 'Recall', 'F-Measure'))
        print('{:<20} {:<20} {:<18}'.format(precision, recall, f_measure))
