
from pprint import pprint # solo para tests

import re
import os
import email
import email.parser
import email.policy

import mrmd.utils as utils
import mrmd.log as log

class RecMail:

    msg = None

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

    def __init__(self, msg):
        unique_date = utils.get_unique_date()
        self.enc_filename = self.dir + unique_date + ".enc"
        self.dec_filename = self.dir + unique_date + ".dec"
        self.sig_filename = self.dir + unique_date + ".sig"

        self.msg = msg
        self.mail_from = msg['from']
        self.mail_to = msg['to']
        self.return_path = msg['Return-Path']
        self.date = msg['Date']
        self.content_type = msg['Content-Type']
        self.subject = msg['subject']

    def getMsg(self):
        return self.msg

    def setMsg(self, msg):
        self.msg = msg

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

    def clear(self, verbose):
        if os.path.exists(self.enc_filename):
            os.remove(self.enc_filename)
        else:
            if verbose >= 2: log.p.info(self.enc_filename + " no existe.")

        if os.path.exists(self.dec_filename):
            os.remove(self.dec_filename)
        else:
            if verbose >= 2: log.p.info(self.dec_filename + " no existe.")

        if os.path.exists(self.sig_filename):
            os.remove(self.sig_filename)
        else:
            if verbose >= 2: log.p.info(self.sig_filename + " no existe.")

    def save_enc(self):
        # print(msg.get_payload()[0].get_payload(decode=True))
        content_type = self.msg.get_payload()[1]['Content-Type']
        match = re.search(r"name=\"(.*)\"", content_type)
        if match: self.enc_realfilename = self.dir + match.groups()[0]
        file = open(self.enc_filename, 'wb')
        try:
            file.write(self.msg.get_payload()[1].get_payload(decode=True))
        except:
            log.p.fail("No se pudo grabar en '" + self.enc_filename + "'.")
        finally:
            file.close()

    def decrypt(self, gpg, passwgpg):
        dec_msg = None
        file = open(self.enc_filename, 'rb')
        try:
            if passwgpg != "": dec_obj = gpg.decrypt_file(file, passphrase=passwgpg)
            else: dec_obj = gpg.decrypt_file(file)

            dec_msg = email.parser.BytesParser(policy=email.policy.default).parsebytes(dec_obj.data, headersonly=False)

            file = open(self.dec_filename, 'wb')
            try:
                file.write(dec_msg.get_payload()[0].get_payload(decode=True))
            except:
                log.p.fail("No se pudo grabar en '" + self.dec_filename + "'.")
            finally:
                file.close()

            file = open(self.sig_filename, 'wb')
            try:
                file.write(dec_msg.get_payload()[1].get_payload(decode=True))
            except:
                log.p.fail("No se pudo grabar en '" + self.sig_filename + "'.")
            finally:
                file.close()
        # except:
        #     log.p.fail("No se pudo leer de '" + self.enc_filename + "'.")
        finally:
            file.close()
