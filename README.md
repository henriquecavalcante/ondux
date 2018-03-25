# ONDUX

ONDUX (On Demand Unsupervised Information Extraction), it is an unsupervised probabilistic approach for IETS problem. It relies on information available on pre-existing data to associate segments in the input string with attributes of a given domain. Unlike other approaches, we rely on very effective matching strategies instead of explicit learning strategies. The effectiveness of this matching strategy is also exploited to disambiguate the extraction of certain attributes through a reinforcement step that explores sequencing and positioning of attribute values directly learned on-demand from test data, with no previous human-driven training, a feature unique to ONDUX.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To use ONDUX you will need to have installed

```
Python 3.6
```

## Running the tests

To perfom the tests on ONDUX, run the following command

```
python ondux knowledgeBase.xml inputFile.txt
```

## Authors

* **Eli Cortez**

## Contributors

* **Henrique Cavalcante**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
