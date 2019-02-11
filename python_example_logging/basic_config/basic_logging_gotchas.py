#! /usr/bin/env python
"""
Using basicConfig has strange behaviour

"""
import logging

SIMPLE_FORMAT= '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


msg = 'Default root logging is WARNING - not printed by info'
logging.info(msg)
logging.warning(msg)

logging.warning('Calling basicConifig with level=logging.INF')
logging.basicConfig(level=logging.INFO, format=SIMPLE_FORMAT)

logging.info('Think this will log?')
logging.error('Wrong! As soon as basicConfig is called it will not run again')


def main():
    print('In the {} main function at the moment.'.format(__file__))
    
    logger.info('Does logger info work')
    logging.info('Does logging info work')

    logger.setLevel(logging.INFO)
    logger.info("Logger now set to info - format still did not work")

    # Set the root logger
    logging.info('still no info logging')

    logging.getLogger().setLevel(logging.DEBUG)
    logging.info('now is logging info.')

    logger.info('still no formatting.')

    logger.debug('only the root logger has debug.')



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format=SIMPLE_FORMAT)

    logger = logging.getLogger(__name__)

    main()
