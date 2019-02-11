"""
package entry point

Calling this directory with python will execute this script.

"""
import logging

SIMPLE_FORMAT= '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


logging.info('this first info is not printed.')
logging.warning('No logging config called yet')

logging.basicConfig(level=logging.INFO, format=SIMPLE_FORMAT)
                
logger = logging.getLogger(__name__)
print('Found main.py')

logger.info('info of %s', __file__)
logger.warning('warning of %s', __file__)

def main():
    print('In the main function at the moment.')
    logger.info('In the main function at the moment.')

    # logger.setLevel(logging.DEBUG)
    logger.debug(logging.basicConfig.__doc__)
    logging.info('default logging')

    import style_app
    import style_app.style
    import style_app.style.main
    #style_app.main()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    logger.setLevel(logging.INFO)
    print('in the __main__ section')
    logger.info('in the __main__ section')

    main()
