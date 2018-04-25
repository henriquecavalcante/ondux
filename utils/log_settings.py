import logging


def initialize_logs():
    '''Initialize global log handler'''
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    return logger
