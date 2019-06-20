# DATEFMT = '%Y-%m-%d %H:%M:%S'
DATEFMT = '%Y-%m-%d %H:%M'
SIMPLE_FORMAT = '%(asctime)s - %(levelname)8s: - %(name)s - %(message)s'
COLOR_FORMAT = '%(asctime)s %(log_color)s- %(levelname)8s:%(reset)s %(name)s - %(message)s'

CUSTOM_COLORS = {  # 'reset' is a color option
            'DEBUG':    'cyan',
            'INFO':     'green',
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'bold_red',
        }
