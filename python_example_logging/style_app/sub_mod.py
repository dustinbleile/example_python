import logging

logger = logging.getLogger(__name__)

def test_basic_logging(msg='test_message'):
    logger.debug(msg)
    logger.info(msg)
    logger.warning(msg)
    logger.error(msg)
    logger.critical(msg)
    