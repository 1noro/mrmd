
import datetime
import re
from optparse import OptionParser

import mrmd.log as log

### FUNCTIONS #################################################################
def options_definition():
    parser = OptionParser()
    parser.add_option(
        "-v", "--verbose", dest="verbose",
        help="print status messages to stdout. There are 3 levels of detail.",
        metavar="LEVEL")
    return parser.parse_args()

def get_new_strtime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_unique_date():
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S-%f")

def get_today():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def get_hour():
    return datetime.datetime.now().strftime("%H:%M:%S")

def get_sec():
    return datetime.datetime.now().strftime("%S")

def get_sendmail_date():
    # return datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z (%Z)")
    return datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0200")
