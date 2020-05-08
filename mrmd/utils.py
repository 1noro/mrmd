# core.utils
# by inoro

### IMPORTS ####################################################################
import datetime

from optparse import OptionParser

import mrmd.log as log
# alternativa:
# import mrmd
# from mrmd import log

### FUNCTIONS ##################################################################
def options_definition():
    parser = OptionParser()
    parser.add_option(
        "-v", "--verbose", dest="verbose",
        help="print status messages to stdout. There are 3 levels of detail.",
        metavar="LEVEL")
    parser.add_option(
        "-m", "--sendmail", dest="sendmail",
        action="store_true", default=False,
        help="send a mail when dynamic ip changes.")
    parser.add_option(
        "-l", "--loop", dest="loop",
        action="store_true", default=False,
        help="run the program in a loop.")
    return parser.parse_args()

def get_new_strtime():
    now = datetime.datetime.now()
    strnow = now.strftime("%Y-%m-%d %H:%M:%S")
    return strnow
