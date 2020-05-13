
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

# -----------------------------------------------------------------------------
def get_sig_blk(str):
    out = ""
    record = False
    lines = str.split("\r\n")
    for line in lines:
        if line == "-----BEGIN PGP SIGNATURE-----": record = True
        if line == "-----END PGP SIGNATURE-----":
            out += line
            break
        if record: out += line + "\r\n"
    return out

def get_msg_blk(str):
    regex = r"boundary=\"(.*)\""
    matches = re.finditer(regex, str, re.MULTILINE)
    for match in matches:
        # print(match.groups()[0])
        for group in match.groups():
            print(group)
    # out = ""
    # record = False
    # lines = str.split("\r\n")
    # for line in lines:
    #     if line == "-----BEGIN PGP SIGNATURE-----": record = True
    #     if line == "-----END PGP SIGNATURE-----":
    #         out += line
    #         break
    #     if record: out += line + "\r\n"
    # return out
