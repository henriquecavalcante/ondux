import hashlib
import logging
import os
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET


def read_input(input_file):
    '''Read input file containing data to be extracted'''
    with open(input_file) as f:
        contents = f.read()
        print(contents)

def normalize_str(input_str):
    '''Transform string to lowercase, remove special chars,
    accents and trailing spaces'''
    byte_string = unicodedata.normalize('NFD',input_str.lower()).encode('ASCII', 'ignore')
    return re.sub(r'[^A-Za-z0-9\s]+', '', byte_string.decode('utf-8')).strip()

def get_hash(text):
    '''Get the MD5 hash from a string'''
    temp  = normalize_str(text)
    return hashlib.sha224(temp.encode()).hexdigest()
