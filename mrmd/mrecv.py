
import imaplib
import email
import email.parser
import email.policy

import mrmd.log as log
from mrmd.RecMailPlain import RecMailPlain

### FUNCTIONS #################################################################
def get_unseen_mails(username, passwgoo, name, verbose):
    mail_arr = []
    conn = imaplib.IMAP4_SSL('imap.gmail.com')
    try:
        (retcode, capabilities) = conn.login(username, passwgoo)
    except:
        log.pt.fail(sys.exc_info()[1], name)
        sys.exit(1)

    conn.select("inbox")
    (retcode, messages) = conn.search(None, '(UNSEEN)')
    if retcode == 'OK' and messages[0] != b'':
        for num in messages[0].split(b' '):
            typ, data = conn.fetch(num,'(RFC822)')
            msg = email.parser.BytesParser(policy=email.policy.default).parsebytes(data[0][1], headersonly=False)
            # comprobamos que el formato del mensaje sea el correcto
            if msg['subject'][:1].lower() == 'r' and msg.get_content_type() == 'text/plain':
                mail_arr.append(RecMailPlain(msg, name))
            # typ, data = conn.store(num,'-FLAGS','\\Seen') # desmarcamaos el mensaje como leido

    conn.close()
    return mail_arr
