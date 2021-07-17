import logging

#All the events either wrong/right, it is fine or not
logging.basicConfig(filename="selenium_logs.log",format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)


logging.info("info")
logging.debug("debutg")
logging.error("error")
logging.critical("critical")
logging.warning("warning")