import logging

def test_basic_logging(msg='test_message'):
    logging.debug(msg)
    logging.info(msg)
    logging.warning(msg)
    logging.error(msg)
    