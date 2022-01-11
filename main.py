import logging

print("test")
logging.basicConfig(filename="logFile",
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

logging.info("Running Urban Planning")

self.logger = logging.getLogger('urbanGUI')
