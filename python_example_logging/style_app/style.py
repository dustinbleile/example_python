#! /usr/bin/env python
"""
Try to use basic PEP style module methods
"""
# standard imports
import argparse
import logging
import logging.config

# non-standard
try:
    import colorlog
    COLORLOG = True
except ModuleNotFoundError:
    COLORLOG = False

# local imports

# Upper level package access
#if __package__:
    # The relative import will work if this has been called like a module
    # eg python -m python_example_logging.style_app.style
try:
    from .. import constants
    from .. import style_app
    print("Succesful local imports")
except ValueError:  # just always adding packages to path seems more reliable
    print("Failed local imports - adding paths")

    import os, sys
    style_app_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
    example_dir = os.path.dirname(style_app_dir)
    print('adding {} to path'.format(example_dir))
    sys.path.insert(0, example_dir)  # insert at begining to get checked first

    from python_example_logging import constants
    from python_example_logging import style_app

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': constants.SIMPLE_FORMAT,
            # 'datefmt': constants.DATEFMT,
        },
        'color': {
            '()': 'colorlog.ColoredFormatter',  # colored output
            'format': constants.COLOR_FORMAT,
            'datefmt': constants.DATEFMT,
            }
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'color': {
            'level': 'INFO',
            'formatter': 'color',
            'class': 'colorlog.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'test.log',
            'formatter': 'standard',
        }
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        },
        __name__: {
            'handlers': ['color'],
            'level': 'DEBUG',
            'propagate': False  # Do not keep propagating up to root
        },
        'python_example_logging': {
            'handlers': ['color'],
            'level': 'DEBUG',
            'propagate': False  # Do not keep propagating up to root
        },
    }
}

logger = logging.getLogger(__name__)


def main():
    logging.config.dictConfig(LOGGING_CONFIG)

    logging.info('root logger info')
    logger.info('style_app: %s', [i for i in dir(style_app) if not i.startswith('__')])
    print('logging style test')
    msg = "sytle::main - test msg"
    logger.setLevel(logging.DEBUG)
    logger.debug(msg)
    logger.info(msg)
    logger.warning(msg)
    logger.error(msg)
    logger.critical(msg)


    print("Trying down_folder")
    logger.info("Starting down_test")

    # Full import
    from python_example_logging.style_app.down_folder import down_test
    down_test.test_basic_logging()

    # Relative import
    logger.info('Starting .sub_mod test')
    from python_example_logging.style_app import sub_mod
    sub_mod.test_basic_logging()

    logger.info('style_app: %s', [i for i in dir(style_app) if not i.startswith('__')])

    return True


def logging_setup():
    # Set root logger to info level
    logging.getLogger().setLevel(logging.INFO)
    # Set up logger
    logger.setLevel(logging.INFO)
    if COLORLOG:
        formatter = colorlog.ColoredFormatter(
            constants.COLOR_FORMAT,
            datefmt=constants.DATEFMT,
            log_colors=constants.CUSTOM_COLORS,
            )
        ch = colorlog.StreamHandler()
    else:
        formatter = logging.Formatter(
            constants.SIMPLE_FORMAT,
            datefmt=constants.DATEFMT)
        ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)


if __name__ == "__main__":
    try:
        # Changing the logger has a big effect.
        logger = logging.getLogger('python_example_logging.style_app')
        logging_setup()
        main()
    except Exception as err:
        logging.critical(err, exc_info=True)
