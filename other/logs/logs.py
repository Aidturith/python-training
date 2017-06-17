'''
Created on 22 avr. 2016

@author: aidturith
'''

# https://docs.python.org/3/howto/logging.html

import logging
logging.basicConfig(format='[%(asctime)s] - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S',
                    level=logging.DEBUG,
                    filename='temp\example.log')


if __name__ == '__main__':
    pass


class __main__(object):
    logging.fatal('oups')
    logging.error('error')
    logging.warning('warn')
    logging.info('info')
    logging.debug('debu')
    logging.debug('%s before you %s', 'Look', 'leap!')
    logging.info('TODO: next step is to look into logging config and handlers (socket, smtp...)')
    logging.debug('debug')
