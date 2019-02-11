#! /usr/bin/env python
"""
Try to use basic PEP style module methods
"""
# standard imports
import argparse
import logging

# non-standard
try:
    import colorlog
    COLORLOG = True
except ModuleNotFoundError:
    COLORLOG = False

# local imports

if __package__:
    # The relative import will work if this has been called like a module
    # eg python -m python_example_logging.style_app.style
    from .. import constants
else:
    import os, sys
    pack_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
    sys.path.insert(0, pack_dir)  # insert at begining to get checked first
    import constants

print(constants.SIMPLE_FORMAT)

logger = logging.getLogger(__name__)


def main():
    print("Trying down_folder")
    logger.info("Starting down_test")

    # Full import
    #from python_example_logging.style_app.down_folder import down_test
    
    from style_app.down_folder import down_test
    down_test.test_basic_logging()

    # Relative import
    logger.info('Starting .sub_mod test')
    import sub_mod
    sub_mod.test_basic_logging()

    logger.info('Starting basicConfig sub_mod test')
    import  python_example_logging.basic_config.sub_mod
    python_example_logging.basic_config.sub_mod.test_basic_logging()

    return True


def logging_setup():
    logger.setLevel(logging.INFO)
    logging.getLogger().setLevel(logging.INFO)


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)

    try:
        logging_setup()
        main()
    except Exception as err:
        logging.critical(err, exc_info=True)
