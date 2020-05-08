
import os

import gnupg

import mrmd
from mrmd import utils
from mrmd import log
from mrmd import mail

### EDITABLE VARIABLES ########################################################
LOGIN_FILE = "docs/login.conf"
MAILSTO_FILE = "docs/mailsto.list"
TABULAR = " "*8

### AUTOMATIC VARIABLES #######################################################
verbose = 0
# version=open("version.txt").read().replace('\n','')
version="0.0.1"
username = ""
passwgoo = ""
passwgpg = ""
mailsto = []

### FUNCTIONS #################################################################
# ...

### MAIN ######################################################################
def main():
    # --- Parameters ----------------------------------------------------------
    (options, args) = utils.options_definition()
    # --- verbose
    verbose = 0
    if options.verbose :
        verbose = int(options.verbose)

    # --- CHECK CONFIG --------------------------------------------------------
    if verbose >= 1: log.p.info("starting  v"+version)
    # --- LOGIN_FILE
    if os.path.isfile(LOGIN_FILE):
        with open(LOGIN_FILE) as f: ncdata = f.read()
        ncdata_rows = ncdata.split('\n')
        username = ncdata_rows[0]
        passwgoo = ncdata_rows[1]
        passwgpg = ncdata_rows[2]
    else:
        log.p.fail("'"+LOGIN_FILE+"' not found")
        sys.exit()

    # --- MAILSTO_FILE
    if os.path.isfile(MAILSTO_FILE):
        with open(MAILSTO_FILE) as f: ncdata = f.read()
        ncdata_rows = ncdata.split('\n')
        for row in ncdata_rows:
            if row != "": mailsto.append(row)
    else:
        log.p.fail("'"+MAILSTO_FILE+"' not found")
        sys.exit()

    # --- EXECUTION -----------------------------------------------------------
    # gpg = gnupg.GPG(gnupghome='/home/cosmo/.gpghome')
    # unencrypted_string = 'Who are you? How did you get in my house?'
    # encrypted_data = gpg.encrypt(unencrypted_string, 'nnoottiiffyy.mm@gmail.com')
    # encrypted_string = str(encrypted_data)
    # print('ok: ', encrypted_data.ok)
    # print('status: ', encrypted_data.status)
    # print('stderr: ', encrypted_data.stderr)
    # print('unencrypted_string: ', unencrypted_string)
    # print('encrypted_string: ', encrypted_string)

    mail.send_rmd(username, passwgoo, mailsto, verbose)

    # --- Exit ----------------------------------------------------------------
    if verbose >= 1: log.p.exit("end of the execution")
