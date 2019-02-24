import logging

logger = logging.getLogger(__name__)

def test_basic_logging(msg='down test_message'):
    print(__name__)
    logger.debug(msg)
    logger.info(msg)
    logger.warning(msg)
    logger.error(msg)
    