#! /gsc/pipelines/envs/default_python
"""
General logging and warning setup.
"""

# Standard Libraries
import argparse
import configparser
import logging
import os
import pdb
import sys
import warnings

# External Libraries
try:
    import colorlog
    COLOR = True
except ImportError:
    COLOR = False

__version__ = 'v0.0.0'

DATEFMT = '%Y-%m-%d %H:%M:%S'
BASIC_LOG_FORMAT = '%(asctime)s %(levelname)-8s: %(message)s'
DETAILED_LOG_FORMAT = BASIC_LOG_FORMAT.replace(
    '%(message)s',
    '- %(name)-12s[%(filename)s:%(lineno)s - %(funcName)20s()] : %(message)s')
COLOR_FORMAT = '%(log_color)s'


def send_warnings_to_logging(message, category, filename, lineno, file_handle=None, extra_var=None):
    """
    Make a function so that warnings.warn sends the message to logger,
    but still does not spam with the same message multiple times.

    Replace warnings.showwarning with this function
    """
    return logging.warning('%s:%s: %s:%s', filename, lineno, category.__name__, message)


def logging_basic_config(level=logging.INFO,
                         format=BASIC_LOG_FORMAT,
                         datefmt=DATEFMT,
                         filename=None,
                         capture_warnings_module=True):
    """
    Setup default basic config style.
    Use logging module if colorlog is not available.
    """
    # Always setup a stream-handler
    if COLOR:  # Only apply color to screen by default, not files
        colorlog.basicConfig(format=COLOR_FORMAT + format, datefmt=datefmt, level=level)
    else:
        logging.basicConfig(format=format, datefmt=datefmt, level=level)
    logging.debug("Logging stream handler setup")

    if filename:  # do not use color for file logging
        if os.path.exists(filename):
            logging.warning("log file already exists at: %s", filename)
        log_handle = logging.FileHandler(filename)
        log_handle.setFormatter(logging.Formatter(format, datefmt=datefmt))
        log_handle.setLevel(level)
        logging.getLogger().addHandler(log_handle)
        logging.info("Logging to file: %s", filename)

    if capture_warnings_module:
        # Override warnings.showwarning with a function to send the message to logging.warning.
        # Preserves the effect where warnings.warn only shows a message once.
        if not hasattr(warnings, 'original_showwarning'):
            warnings.original_showwarning = warnings.showwarning
            warnings.showwarning = send_warnings_to_logging


def main():
    colorlog.debug("Which logging format do we have?")


if __name__ == '__main__':
    # Parse parameters
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description=__doc__,
    )
    parser.add_argument('-i', '--patient-id', help='Patient id (eg. POG129)')
    parser.add_argument('-c', '--config', help='Config file with patient and data info')
    parser.add_argument('-v', '--version',
                        help='Display verions and exit',
                        action='version',
                        version='{} {}'.format(parser.prog, __version__))

    parser.add_argument('--logfile', help='logging filename')
    log_level = parser.add_mutually_exclusive_group()
    log_level.add_argument('--debug', action='store_true', help="Debug level info printed to screen.  More verbose.")
    log_level.add_argument('--quiet', action='store_true', help="Only warnings and errors printed to screen.  Less verbose.")

    args = parser.parse_args()

    os.umask(2)  # Default to User and Group Read/Write

    # Set up logging
    if args.logfile:
        args.logfile = os.path.abspath(os.path.realpath(args.logfile))

    if args.debug:
        logging_basic_config(level=logging.DEBUG, format=DETAILED_LOG_FORMAT, filename=args.logfile)
    elif args.quiet:
        logging_basic_config(level=logging.WARNING, filename=args.logfile)
    else:
        logging_basic_config(level=logging.INFO, filename=args.logfile)

    if args.debug:
        logging.debug("Verbose logging set")
    if args.logfile:
        logging.info("Command run: '{}'".format(' '.join(sys.argv)))
        logging.info("Script file: '%s'", os.path.abspath(os.path.realpath(__file__)))

    # Call programs
    main()

    if args.logfile:
        logging.info("Logged to file: %s", args.logfile)
