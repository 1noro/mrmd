
import os
import threading
import gnupg

import mrmd
from mrmd import utils
from mrmd import log
from mrmd import msend
from mrmd import mrecv
from mrmd import gpg

### EDITABLE VARIABLES ########################################################
LOGIN_FILE = "config/login.conf"
MAILSTO_FILE = "config/mailsto.list"
RMD_DIR = "tmp/"
TABULAR = " " * 8

### AUTOMATIC VARIABLES #######################################################
verbose = 0
# version=open("version.txt").read().replace('\n','')
version="0.0.1"
username = ""
passwgoo = ""
passwgpg = ""
mailsto = []
# mygnupghome = os.environ['HOME'] + "/.gnupg"
mygnupghome = os.environ['HOME'] + "/.gpgpy"

### FUNCTIONS #################################################################
def check_mail(gpg, username, passwgoo, passwgpg, RMD_DIR, name, verbose):
    # leemos los correos nuevos
    mail_arr = mrecv.get_unseen_mails(username, passwgoo, name, verbose)
    # procesamos los emails recibidos uno a uno
    for mail in mail_arr:
        log.pt.info("Procesando mail " + mail.getId(), )
        if mail.getValid():
            mail.verify(gpg, passwgpg, name, verbose)
            if mail.getVerified(): mail.save_rmd(gpg, passwgpg, RMD_DIR, name, verbose)

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
    # abrimos nuestro depósito de claves gpg
    gpg = gnupg.GPG(gnupghome=mygnupghome)
    check_mail_t = threading.Thread(target=check_mail, args=(gpg, username, passwgoo, passwgpg, RMD_DIR, "ck_m", verbose))

    check_mail_t.start()

    # --- Exit ----------------------------------------------------------------
    if verbose >= 1: log.p.exit("end of the execution")
