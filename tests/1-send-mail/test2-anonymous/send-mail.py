
### IMPORTS ####################################################################
import socket
import base64
import datetime

### GLOBAL VARIABLES ###########################################################
subject = b'Esto es una prueba3'
text = b'LOLOLOLOLO3'
host = 'gmail-smtp-in.l.google.com'
bhost = host.encode('utf-8')
port = 25

with open('mailfrom.txt') as f: mailfrom = f.read()
mailto = mailfrom.replace('\n','').encode('utf-8')
with open('mailto.txt') as f: mailto = f.read()
mailto = mailto.replace('\n','').encode('utf-8')

### FUNCTIONS ##################################################################
def by_b64(by):
    b64 = base64.b64encode(by)
    return b64

def mysend(sock, sdata, expected):
    print('[--> ] ', repr(sdata))
    sock.sendall(sdata)
    rdata = sock.recv(1024)
    print('[ <--] ', repr(rdata))
    if rdata.decode("utf-8")[:3] != expected:
        print('[FAIL] '+expected+' reply not received from server')

def myonlysend(sslsock, sdata):
    print('[--> ] ', repr(sdata))
    sslsock.sendall(sdata)

### EXEC #######################################################################
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

rdata = sock.recv(1024)
print('[ <--] ', str(rdata))
if rdata.decode("utf-8")[:3] != '220':
    print('[FAIL] 220 reply not received from server')

mysend(sock,b'EHLO '+bhost+b'\r\n','250')
mysend(sock,b'MAIL FROM: <' + mailfrom + b'>\r\n','250')
mysend(sock,b'RCPT TO: <' + mailto + b'>\r\n','250')
mysend(sock,b'DATA\r\n','354')
now = datetime.datetime.now()
bnow = now.strftime("%a, %d %b %Y %H:%M:%S -0700 (PDT)").encode('utf-8')
myonlysend(sock,b'Date: ' + bnow + b'\r\n')
myonlysend(sock,b'From: ' + mailfrom + b'\r\n')
myonlysend(sock,b'Subject: ' + subject + b'\r\n')
myonlysend(sock,b'\r\n')
myonlysend(sock,text + b'\r\n')
myonlysend(sock,b'.\r\n')
mysend(sock,b'QUIT\r\n','250')

sock.close()
