
import os
import threading
import gnupg
from os import listdir
from os.path import isfile, join

import mrmd
from mrmd import utils
from mrmd import log
from mrmd import msend
from mrmd import mrecv
from mrmd import gpg

### EDITABLE VARIABLES ########################################################
LOGIN_FILE = "config/login.conf"
MAILSTO_FILE = "config/mailsto.list"
RMD_DIR = "rmd/"
TABULAR = " " * 8

### AUTOMATIC VARIABLES #######################################################
verbose = 0
# version=open("version.txt").read().replace('\n','')
version="0.0.2"
username = ""
passwgoo = ""
passwgpg = ""
mailsto = []
# mygnupghome = os.environ['HOME'] + "/.gnupg"
mygnupghome = os.environ['HOME'] + "/.gpgpy"

### FUNCTIONS #################################################################
def check_mails(gpg, username, passwgoo, passwgpg, RMD_DIR, name, verbose):
    # leemos los correos nuevos
    mail_arr = mrecv.get_unseen_mails(username, passwgoo, name, verbose)
    # procesamos los emails recibidos uno a uno
    for mail in mail_arr:
        log.pt.info("Procesando mail " + mail.getId(), )
        if mail.getValid():
            mail.verify(gpg, passwgpg, name, verbose)
            if mail.getVerified(): mail.save_rmd(gpg, passwgpg, RMD_DIR, name, verbose)

def check_reminders(gpg, username, passwgoo, passwgpg, RMD_DIR, name, verbose):
    # metemos en una lista todos los archivos de la carpeta de recordatorios
    all_rmd = [f for f in listdir(RMD_DIR) if isfile(join(RMD_DIR, f))]
    now_rmd = []
    # comprobamos cuales de los recordatorios tenemos que enviar ahora
    for rmd_filename in all_rmd:
        parts = rmd_filename.split('_')
        if parts[0] <= utils.get_today() and parts[1] <= utils.get_hour():
            now_rmd.append(rmd_filename)
    print(now_rmd)

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
    check_mails_t = threading.Thread(target=check_mails, args=(gpg, username, passwgoo, passwgpg, RMD_DIR, "ck_m", verbose))
    check_reminders_t = threading.Thread(target=check_reminders, args=(gpg, username, passwgoo, passwgpg, RMD_DIR, "ck_r", verbose))

    # check_mails_t.start()
    check_reminders_t.start()

    # --- Exit ----------------------------------------------------------------
    if verbose >= 1: log.p.exit("end of the execution")
