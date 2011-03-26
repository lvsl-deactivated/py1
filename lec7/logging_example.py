# codinf: utf-8

import logging
import logging.handlers

def main():
    h = logging.handlers.RotatingFileHandler('test.log', maxBytes=1024*1024*200, backupCount=7)
    h.setFormatter(logging.Formatter('%(asctime)s %(levelname)s (%(module)s) %(message)s'))

    log = logging.getLogger('test')
    log.addHandler(h)
    log.setLevel(logging.DEBUG)

    log.debug('lololo')
    log.info('test')
    log.error('asds')


if __name__ == "__main__":
    main()
