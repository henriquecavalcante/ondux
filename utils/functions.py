import logging
import os
import sys
import unicodedata
import xml.etree.ElementTree as ET


def read_input(input_file):
    '''Read input file containing data to be extracted'''
    with open(input_file) as f:
        contents = f.read()
        print(contents)

def clear_string(input_str):
    '''Transform string to lowercase, remove special chars,
    accents and trailing spaces'''
    byte_string = unicodedata.normalize('NFKD',input_str.lower().strip()).encode('ASCII', 'ignore')
    return byte_string.decode('utf-8')
