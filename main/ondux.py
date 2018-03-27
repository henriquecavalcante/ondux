import os
import sys
import logging
import xml.etree.ElementTree as ET

def parse_kb(kb_file):
    tree = ET.parse(kb_file)
    root = tree.getroot()
    print(root)

def read_input(input_file):
    with open(input_file) as f:
        contents = f.read()
        print(contents)

def run_blocking():
    pass

def run_matching():
    pass

def run_reinforcement():
    pass

def main(knowledge_base, input_file):
    parse_kb(knowledge_base)
    read_input(input_file)
    run_blocking()
    run_matching()
    run_reinforcement()

if __name__ == "__main__":
    # calling main function
    knowledge_base = sys.argv[1]
    input_file = sys.argv[2]
    main(knowledge_base, input_file)