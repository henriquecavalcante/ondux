class Attribute:
    '''
    Represent the attributes that will be used to label blocks
    during the extraction process.

    Attributes have the following properties:
        name: A string representing the attribute's name.
        value: A string representing the attribute's value.
    '''
    def __init__(self, name, value):
        self.name = name
        self.value = value