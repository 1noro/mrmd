
import smtplib
from email.message import Message
from email.header import Header

import mrmd.log as log
import mrmd.utils as utils

### FUNCTIONS #################################################################
def send_rmd_plain(gmail_user, gmail_password, gpg, passwgpg, rmd_filename, name, verbose):
    rmd_cont = ""
    try:
        file = open(rmd_filename, 'rb')
        rmd_cont = file.read().decode('utf-8')
        file.close()
        if verbose >= 3: log.pt.ok("Se ha leido " + rmd_filename + ".", name)
    except:
        log.pt.fail("No se pudo leer '" + rmd_filename + "'.", name)

    if rmd_cont != "":
        rmd_lines = rmd_cont.split('\n')

        to = rmd_lines[0]
        date = utils.get_sendmail_date()
        sent_from = gmail_user

        msg = Message()
        h = Header(rmd_lines[1], 'utf-8')
        msg['Subject'] = h
        subject = msg.as_string().replace('\n\n', '')

        rmd_lines.remove(rmd_lines[0])
        rmd_lines.remove(rmd_lines[0])

        rmd_msg = ""
        for line in rmd_lines: rmd_msg += line + '\n'
        body = rmd_msg.encode("utf-8")[:-2]

        if passwgpg != "": body = gpg.encrypt(body, to, sign=gmail_user, passphrase=passwgpg)
        else: body = gpg.encrypt(body, to, sign=gmail_user)

        # "Subject: " + subject + "\r\n" \
        email_text =    "" + subject + "\r\n" \
                        "From: " + sent_from + "\r\n" \
                        "To: " + to + "\r\n" \
                        "Date: " + date + "\r\n" \
                        "Content-Type: text/plain; charset=\"UTF-8\"\r\n" \
                        "User-Agent: mrmd\r\n" \
                        "MIME-Version: 1.0\r\n" \
                        "\r\n" \
                        "" + body.data.decode('utf-8') + ""

        print(email_text)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()
            if verbose >= 2: log.pt.ok('Email enviado para ' + rmd_filename + '.', name)
        except:
            log.pt.fail('Algo fue mal, el email para ' + rmd_filename + ' NO fué enviado.', name)

# ------------------------------------------------------------------------------
def send_rmd_test(gmail_user, gmail_password, passwgpg, mailsto, gpg, verbose):
    to = ""
    if len(mailsto) > 1: to = ", ".join(mailsto)
    else: to = mailsto[0]

    now = datetime.datetime.now()
    strnow = now.strftime("%a, %d %b %Y %H:%M:%S -0700 (PDT)")

    sent_from = gmail_user
    subject = "COSA: " + strnow
    body = "Hola, esto está cifrado.".encode("utf-8")


    if passwgpg != "": body = gpg.encrypt(body, mailsto[0], sign=gmail_user, passphrase=passwgpg)
    else: body = gpg.encrypt(body, mailsto[0], sign=gmail_user)
    body = str(body)

    email_text =    "From: " + sent_from + "\r\n" \
                    "To: " + to + "\r\n" \
                    "Subject: " + subject + "\r\n" \
                    "\r\n" \
                    "" + body + ""

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print('Email sent!')
    except:
        print('Something went wrong...')
