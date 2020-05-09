
import re

import mrmd.utils as utils

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

        # print(*msg.items(), sep = "\n")

        # for part in msg.iter_attachments():
        #     print(part)
        #     print("-" * 78)

        # print(msg.get_payload()[0].get_payload(decode=True))
        content_type = msg.get_payload()[1]['Content-Type']
        match = re.search(r"name=\"(.*)\"", content_type)
        if match: self.enc_realfilename = self.dir + match.groups()[0]
        open(self.enc_filename, 'wb').write(msg.get_payload()[1].get_payload(decode=True))

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
