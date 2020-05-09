
class RecMail:

    msg = None
    mail_from = ""
    mail_to = ""

    def __init__(self, msg):
        print(type(msg))
        self.msg = msg
        # print(msg.get_body(preferencelist=('related', 'plain', 'html')))
        # print(msg.get_body(preferencelist=('plain')))

    def getMsg(self):
        return self.msg

    def setMsg(self, msg):
        self.msg = msg

    def __repr__(self):
        return  "From: " + self.mail_from + "\n" \
                "To: " + self.mail_to + ""

    def __str__(self):
        return "Aún no implementado."
