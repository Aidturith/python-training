'''
Created on 22 avr. 2016

@author: aidturith
'''

# https://docs.python.org/3/howto/logging.html

import logging


if __name__ == '__main__':
    pass


class __main__(object):
    logging.fatal('oups')
    logging.error('error')
    logging.warning('warn')
    logging.info('info')
    logging.debug('debu')
    
    # log to file
    logging.basicConfig(filename='example.log', level=logging.DEBUG)
    logging.debug('debug')

    # change level and format
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    logging.debug('%s before you %s', 'Look', 'leap!')
    
    # logging time!
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.debug('TODO: next step is to look into logging config and handlers (socket, smtp...)')
    