
import logging

def get_logger(module=__name__, loglevel=logging.INFO):
    FORMAT = '%(asctime)-15s  %(lineno)-3s %(module)-8s %(message)s '
    logging.basicConfig(format=FORMAT)

    logger = logging.getLogger(module)
    logger.setLevel(loglevel)
    # logger.addHandler(logging.StreamHandler())
    return logger
