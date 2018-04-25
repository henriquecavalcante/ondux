import hashlib
import logging
import os
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)

def read_input(input_file):
    '''Read input file containing data to be extracted'''
    try:
        with open(input_file, 'r') as f:
            return f.read().splitlines()
    except IOError as error:
        logger.error('It was not possible to read input file. Cause: ' + error.strerror)
        logger.info('Ondux stopped running!')
        sys.exit(1)

def read_k_base(kb_file):
    '''Parse Knowledge Base XML file'''
    try:
        tree = ET.parse(kb_file)
        return tree.getroot()
    except ET.ParseError as error:
        logger.error('It was not possible to parse knowledge base file. Cause: ' + error.msg)
        logger.info('Ondux stopped running!')
        sys.exit(1)

def normalize_str(input_str):
    '''Transform string to lowercase, remove special chars,
    accents and trailing spaces'''
    byte_string = unicodedata.normalize('NFD',input_str.lower()).encode('ASCII', 'ignore')
    normalized = re.sub(r'[^A-Za-z0-9\s]+', '', byte_string.decode('utf-8')).strip()
    if re.match(r'^\d+\s\d+$', normalized):
        return re.sub(r' ', '', normalized)
    return normalized

def get_hash(text):
    '''Get the MD5 hash from a string'''
    temp  = normalize_str(text)
    return hashlib.sha224(temp.encode()).hexdigest()

def get_stop_words():
    '''Get a list with Portuguese and English stop words'''
    try:
        with open('./res/en_stop_words.txt', 'r') as f:
            stop_words = f.read().splitlines()
        with open('./res/pt_stop_words.txt', 'r') as f:
            stop_words += f.read().splitlines()
        return stop_words
    except IOError as error:
        logger.error('It was not possible to read stop words file. Cause: ' + error.strerror)
        logger.info('Ondux stopped running!')
        sys.exit(1)

def remove_stop_words(text):
    '''Remove the stop words of a string and return the list of tokens'''
    return ' '.join([word for word in text.split() if word not in get_stop_words()])
