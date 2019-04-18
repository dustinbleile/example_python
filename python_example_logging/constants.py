DATEFMT = '%Y-%m-%d %H:%M:%S'
SIMPLE_FORMAT = '%(asctime)s - %(name)s - %(levelname)8s: %(message)s'
COLOR_FORMAT = '%(asctime)s - %(log_color)s%(name)s - %(levelname)8s%(reset)s: %(message)s'

CUSTOM_COLORS = {  # 'reset' is a color option
            'DEBUG':    'cyan',
            'INFO':     'green',
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'bold_red',
        }