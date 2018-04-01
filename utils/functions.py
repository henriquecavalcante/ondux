import os, sys
import logging
import  unicodedata
import xml.etree.ElementTree as ET

def parse_kb(kb_file):
    '''Parse Knowledge Base and prepare it to extract
    the content-based features'''
    tree = ET.parse(kb_file)
    root = tree.getroot()
    for item in root:
        print(clear_string(item.tag), clear_string(item.text))

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
