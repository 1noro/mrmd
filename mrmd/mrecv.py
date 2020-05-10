
import datetime # creo que es prescindible

import imaplib
import email
import email.parser
import email.policy

import mrmd.log as log
import mrmd.RecMail
from mrmd.RecMail import RecMail
from mrmd.RecMailPlain import RecMailPlain

### FUNCTIONS #################################################################
def get_unseen_mails(username, passwgoo, verbose):
    mail_arr = []
    conn = imaplib.IMAP4_SSL('imap.gmail.com')
    try:
        (retcode, capabilities) = conn.login(username, passwgoo)
    except:
        print(sys.exc_info()[1])
        sys.exit(1)

    conn.select("inbox")
    (retcode, messages) = conn.search(None, '(UNSEEN)')
    if retcode == 'OK' and messages[0] != b'':
        for num in messages[0].split(b' '):
            typ, data = conn.fetch(num,'(RFC822)')
            msg = email.parser.BytesParser(policy=email.policy.default).parsebytes(data[0][1], headersonly=False)
            # comprobamos que el formato del mensaje sea el correcto
            if msg['subject'] == 'r' and (msg.get_content_type() == 'multipart/encrypted' or msg.get_content_type() == 'multipart/signed'):
                mail_arr.append(RecMail(msg))
            elif msg['subject'] == 'r' and msg.get_content_type() == 'text/plain':
                mail_arr.append(RecMailPlain(msg))
            typ, data = conn.store(num,'-FLAGS','\\Seen') # desmarcamaos el mensaje como leido
            # typ, data = conn.store(num,'+FLAGS','\\Seen') # marcamos como leido el mensaje (no hace falta, es automático)

    conn.close()
    return mail_arr

# -----------------------------------------------------------------------------
def recv_rmd_test(username, passwgoo, passwgpg, mygpg, verbose):
    # mail = imaplib.IMAP4_SSL('imap.gmail.com')
    # mail.login(username, passwgoo)
    # # print(mail.list())
    # # Out: list of "folders" aka labels in gmail.
    # mail.select("inbox") # connect to inbox.
    #
    # result, data = mail.search(None, "ALL")
    #
    # ids = data[0] # data is a list.
    # id_list = ids.split() # ids is a space separated string
    # latest_email_id = id_list[-1] # get the latest
    #
    # result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
    #
    # raw_email = data[0][1] # here's the body, which is raw text of the whole email
    # # including headers and alternate payloads
    # print(raw_email.decode("utf-8"))

    # leer solo los mensajes no leidos de la bandeja de entrada
    conn = imaplib.IMAP4_SSL('imap.gmail.com')
    try:
        (retcode, capabilities) = conn.login(username, passwgoo)
    except:
        print(sys.exc_info()[1])
        sys.exit(1)

    # conn.select(readonly=1) # Select inbox or default namespace
    conn.select("inbox") # Select inbox or default namespace
    (retcode, messages) = conn.search(None, '(UNSEEN)')
    if retcode == 'OK' and messages[0] != b'':
        for num in messages[0].split(b' '):
            print('Processing :', num)
            typ, data = conn.fetch(num,'(RFC822)')
            msg = email.message_from_string(data[0][1].decode("utf-8"))
            typ, data = conn.store(num,'-FLAGS','\\Seen')
            print(data,'\n',30*'-')
            print(msg)

    conn.close()
