import logging

#logging levels
#debug()
#info()
#warning()
#error()
#critical()

logging.basicConfig(level = logging.WARNING, format = '%(asctime)s - %(levelname)s: %(message)s')
logging.debug('logging message, DEBUG') #Ignored since level is set to WARNING
logging.info('logging message, INFO') #Ignored since level is set to WARNING
logging.warning('logging message, WARNING') #Start printing here
logging.error('logging message, ERROR')
logging.critical('logging message, CRITICAL')

#asctime - Operation time
#levelname - print level
