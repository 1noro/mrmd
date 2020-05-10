
from pprint import pprint # solo para tests

import re
import os
import email
import email.parser
import email.policy

import mrmd.utils as utils
import mrmd.log as log

class RecMailPlain:

    msg = None
    id = ""

    mail_from = ""
    mail_to = ""
    return_path = ""
    date = ""
    content_type = ""
    subject = ""

    dir = "tmp/"
    enc_filename = ""
    enc_realfilename = ""
    dec_filename = ""
    sig_filename = ""
    sig_realfilename = ""

    valid = False
    verified = False

    def __init__(self, msg):
        self.id = utils.get_unique_date()
        self.enc_filename = self.dir + self.id + ".enc"
        self.dec_filename = self.dir + self.id + ".dec"
        self.sig_filename = self.dir + self.id + ".sig"

        self.msg = msg
        self.mail_from = msg['from']
        self.mail_to = msg['to']
        self.return_path = msg['Return-Path']
        self.date = msg['Date']
        self.content_type = msg['Content-Type']
        self.subject = msg['subject']

        msg_cont_enc = self.msg.get_content()
        pattern = re.compile("-----BEGIN PGP MESSAGE-----")
        if pattern.match(msg_cont_enc):
            log.p.ok("El mensaje " + self.id + " está encriptado.")
            valid = True
        else:
            log.p.fail("El mensaje " + self.id + " NO está encriptado.")

    def getMsg(self):
        return self.msg

    def setMsg(self, msg):
        self.msg = msg

    def getId(self):
        return self.id

    def getValid(self):
        return self.valid

    def getVerified(self):
        return self.verified

    def __repr__(self):
        return  "From: " + self.mail_from + "\n" \
                "To: " + self.mail_to + "\n" \
                "Return-Path: " + self.return_path + "\n" \
                "Date: " + self.date + "\n" \
                "Content-Type: " + self.content_type + "\n" \
                "Subject: " + self.subject + ""

    def __str__(self):
        return str(self.msg)

    # -------------------------------------------------------------------------

    def decrypt(self, gpg, passwgpg):
        dec_msg = None

        # if passwgpg != "": dec_obj = gpg.decrypt(file, passphrase=passwgpg)
        # else: dec_obj = gpg.decrypt(file)

    def verify(self, gpg):
        # gpg --sign -u <user> --armor --detach-sign <doc>
        # gpg --verify <doc.sig> <doc>
        file = open(self.enc_filename, 'rb')
        try:
            # verified = gpg.verify_file(file, self.dec_filename)
            verified = gpg.verify_file(file)
            # pprint(dir(verified))
            print(verified.stderr) # no se firma bien, ¿porqué?
            # if verified.username != None:
            #     self.verified = True
        # except:
        #     log.p.fail("No se pudo leer de '" + self.sig_filename + "'.")
        finally:
            file.close()
