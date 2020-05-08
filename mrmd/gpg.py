
import gnupg
from pprint import pprint

import mrmd.log as log

### FUNCTIONS #################################################################
def test(mygnupghome, username, passwgpg, verbose):
    mygpg = gnupg.GPG(gnupghome=mygnupghome)
    unencrypted_string = 'Who are you? How did you get in my house?'
    encrypted_data = mygpg.encrypt(unencrypted_string, username)
    encrypted_string = str(encrypted_data)
    if verbose >= 3: print('ok: ', encrypted_data.ok)
    if verbose >= 3: print('status: ', encrypted_data.status)
    if verbose >= 3: print('stderr: ', encrypted_data.stderr)
    if verbose >= 1: print('unencrypted_string: ', unencrypted_string)
    if verbose >= 1: print('encrypted_string: ', encrypted_string)

    if passwgpg != "":
        decrypted_data = mygpg.decrypt(encrypted_string, passphrase=passwgpg)
    else:
        decrypted_data = mygpg.decrypt(encrypted_string)

    if verbose >= 3: print('ok: ', decrypted_data.ok)
    if verbose >= 3: print('status: ', decrypted_data.status)
    if verbose >= 3: print('stderr: ', decrypted_data.stderr)
    if verbose >= 1: print('decrypted string: ', decrypted_data.data)
