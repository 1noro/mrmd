
import re

import mrmd.utils as utils

class RecMail:

    msg = None
    mail_from = ""
    mail_to = ""
    enc_filename = ""
    enc_realfilename = ""

    def __init__(self, msg):
        self.enc_filename = utils.get_unique_date() + ".enc"
        # print(type(msg))
        # print(msg)
        self.msg = msg

        # print(msg.get_body(preferencelist=('related', 'plain', 'html')))
        # print(msg.get_body(preferencelist=('plain')))

        # print(msg['from'])
        # print(msg['to'])
        # print(msg['subject'])

        # print(*msg.items(), sep = "\n")

        # for part in msg.iter_attachments():
        #     print(part)
        #     print("-" * 78)

        if msg.get_content_type() == 'multipart/encrypted':
            # print(msg.get_payload()[0].get_payload(decode=True))
            content_type = msg.get_payload()[1]['Content-Type']
            match = re.search(r"name=\"(.*)\"", content_type)
            if match: self.enc_realfilename = match.groups()[0]
            open('tmp/' + self.enc_filename, 'wb').write(msg.get_payload()[1].get_payload(decode=True))

    def getMsg(self):
        return self.msg

    def setMsg(self, msg):
        self.msg = msg

    def __repr__(self):
        return  "From: " + self.mail_from + "\n" \
                "To: " + self.mail_to + ""

    def __str__(self):
        return "Aún no implementado."
