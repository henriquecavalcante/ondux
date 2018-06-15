# ONDUX

This is a Python implementation of ONDUX (On Demand Unsupervised Information Extraction). It is an unsupervised probabilistic approach for IETS problem. It relies on information available on pre-existing data (knowledge base) to associate segments in the input string with attributes of a given domain.

Reference: https://dl.acm.org/citation.cfm?id=1807254

## Requirements

To use ONDUX you will need to have installed

```
Python 3.6
```

## Execution Instructions

To perform tests on ONDUX method, open the project folder on the terminal and type the following command:

```
python ondux.py /path/to/knowledge_base_file.xml /path/to/input_file.txt /path/to/reference_file.xml
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
