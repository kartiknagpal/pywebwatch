from config import url_to_check
import logging
# create logger
lgr = logging.getLogger(url_to_check)
lgr.setLevel(logging.DEBUG)
# add a file handler
fh = logging.FileHandler('Webwatch.log')
# create a formatter and set the formatter for the handler.
frmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(frmt)
# add the Handler to the logger
lgr.addHandler(fh)