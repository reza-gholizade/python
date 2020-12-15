#!/usr/bin/python3.6
import sys
import logging
from logging.config import dictConfig

LOG_PATH = '/var/log/backup.log'
logging_config = dict(
    version=1,
    formatters={
        'verbose': {
            'format': ("[%(asctime)s] %(levelname)s "
                       "%(message)s"),
            'datefmt': "%d/%b/%Y %H:%M:%S",
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
    },
    handlers={
        'log': {'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'verbose',
                'level': logging.DEBUG,
                'filename': LOG_PATH,
                'maxBytes': 52428800,
                'backupCount': 7},
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'stream': sys.stdout,
        },
    },
    loggers={
        'log': {
            'handlers': ['log', 'console'],
            'level': logging.DEBUG
        }
    }
)

dictConfig(logging_config)

log = logging.getLogger('log')

