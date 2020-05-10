
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

    msg_cont_enc = ""

    valid = False
    verified = False

    def __init__(self, msg):
        self.id = utils.get_unique_date()

        self.msg = msg
        self.mail_from = msg['from']
        self.mail_to = msg['to']
        self.return_path = msg['Return-Path']
        self.date = msg['Date']
        self.content_type = msg['Content-Type']
        self.subject = msg['subject']

        self.msg_cont_enc = msg.get_content()
        pattern = re.compile("-----BEGIN PGP MESSAGE-----")
        if pattern.match(self.msg_cont_enc):
            # log.p.ok("El mensaje " + self.id + " está encriptado.")
            self.valid = True
        else:
            log.p.fail("El mensaje " + self.id + " NO está encriptado.")

    def getMsg(self):
        return self.msg

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
        dec_obj = None
        if passwgpg != "": dec_obj = gpg.decrypt(self.msg_cont_enc, passphrase=passwgpg)
        else: dec_obj = gpg.decrypt(self.msg_cont_enc)
        # print(dec_obj.stderr)
        return dec_obj.data

    def verify(self, gpg, passwgpg, verbose):
        verified = False
        # probamos a verificar con la firma junoto al mensaje desencriptado (BEGIN PGP SIGNED MESSAGE)
        verified = gpg.verify(self.decrypt(gpg, passwgpg))
        # print(verified.stderr)
        if verified:
            if verbose >= 2: log.p.ok("El mensaje " + self.id + " está verificado.")
            self.verified = True
        else:
            # probamos a verificar con la firma en el propio mensaje encriptado
            dec_obj = None
            if passwgpg != "": dec_obj = gpg.decrypt(self.msg_cont_enc, passphrase=passwgpg)
            else: dec_obj = gpg.decrypt(self.msg_cont_enc)
            if dec_obj.trust_level is not None and dec_obj.trust_level >= dec_obj.TRUST_FULLY:
                if verbose >= 2: log.p.ok("El mensaje " + self.id + " está verificado.")
                self.verified = True
            else:
                log.p.fail("El mensaje " + self.id + " NO está verificado o el nivel de confianza no es el adecuado.")

    def rm_sig_msg_head(self, txt):
        record = False
        out = ""
        txt_lines = txt.split('\n')
        for line in txt_lines:
            if record: out += line + '\n'
            if (not record) and line == "": record = True
        return out

    def rm_mail_sig(self, txt_lines):
        record = True
        out = []
        for line in txt_lines:
            if record and (line == "- -- " or line == "-- "): record = False
            if record: out.append(line)
        return out

    def save_rmd(self, gpg, passwgpg, dir, verbose):
        dec_msg = self.decrypt(gpg, passwgpg).decode('utf-8')
        dec_msg_lines = None
        pattern = re.compile("-----BEGIN PGP SIGNED MESSAGE-----")
        if pattern.match(dec_msg):
            if verbose >= 3: log.p.info("El mensaje " + self.id + " es del tipo: BEGIN PGP SIGNED MESSAGE.")
            dec_msg = self.rm_sig_msg_head(dec_msg)
        dec_msg = dec_msg.replace('\r', '')
        dec_msg_lines = dec_msg.split('\n')
        dec_msg_lines = self.rm_mail_sig(dec_msg_lines)

        day = dec_msg_lines[0]
        hour = dec_msg_lines[1]
        subjetc = dec_msg_lines[2]

        dec_msg_lines.remove(day)
        dec_msg_lines.remove(hour)
        dec_msg_lines.remove(subjetc)

        for line in dec_msg_lines:
            print("linea:", line)
