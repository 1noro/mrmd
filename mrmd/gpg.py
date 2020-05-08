
import gnupg
from pprint import pprint
import quopri

import mrmd.log as log
import mrmd.utils as utils

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

def test2(mygnupghome, username, passwgpg, verbose):
    mygpg = gnupg.GPG(gnupghome=mygnupghome)
    encrypted_string = """-----BEGIN PGP MESSAGE-----

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
q1JPhEcoq+Wojk3O8GYnef7o9lQVmig=
=LyFf
-----END PGP MESSAGE-----"""

    if passwgpg != "":
        decrypted_data = mygpg.decrypt(encrypted_string, passphrase=passwgpg)
    else:
        decrypted_data = mygpg.decrypt(encrypted_string)

    if verbose >= 3: print('ok: ', decrypted_data.ok)
    if verbose >= 3: print('status: ', decrypted_data.status)
    if verbose >= 3: print('stderr: ', decrypted_data.stderr)
    if verbose >= 1: print('decrypted string: ', decrypted_data.data.decode("utf-8"))

def test3(mygnupghome, username, passwgpg, verbose):
    mygpg = gnupg.GPG(gnupghome=mygnupghome)
    unencrypted_string = 'Hola, esto es una prueba.'
    if verbose >= 1: print('unencrypted_string: ', unencrypted_string)
    print("-" * 72)

    if passwgpg != "": signed_data = mygpg.sign(unencrypted_string, keyid=username, passphrase=passwgpg)
    else: signed_data = mygpg.sign(unencrypted_string, keyid=username)

    if verbose >= 1: print('signed_data: ', signed_data)
    print("-" * 72)

    encrypted_data = mygpg.encrypt(str(signed_data), username)
    encrypted_string = str(encrypted_data)

    if verbose >= 3: print('ok: ', encrypted_data.ok)
    if verbose >= 3: print('status: ', encrypted_data.status)
    if verbose >= 3: print('stderr: ', encrypted_data.stderr)
    print("-" * 72)
    if verbose >= 1: print('encrypted_string: ', encrypted_string)
    print("-" * 72)

    if passwgpg != "": decrypted_data = mygpg.decrypt(encrypted_string, passphrase=passwgpg)
    else: decrypted_data = mygpg.decrypt(encrypted_string)

    if verbose >= 3: print('ok: ', decrypted_data.ok)
    if verbose >= 3: print('status: ', decrypted_data.status)
    if verbose >= 3: print('stderr: ', decrypted_data.stderr)
    print("-" * 72)
    if verbose >= 1: print('decrypted string: ', decrypted_data.data.decode("utf-8"))
    print("-" * 72)

    verified = mygpg.verify_file(io.BytesIO(encrypted_data.data))
    if not verified: print("ERROR: Signature could not be verified!")
    if verbose >= 1: print('verifyed by: ', verified.username)

# encriptado: OK, firmado: OK
def test4(mygnupghome, username, passwgpg, verbose):
    mygpg = gnupg.GPG(gnupghome=mygnupghome)
    unencrypted_string = 'Hola, esto es una prueba.'
    if verbose >= 1: print('unencrypted_string: ', unencrypted_string)
    print("-" * 72)

    if passwgpg != "": encrypted_data = mygpg.encrypt(unencrypted_string, username, sign=username, passphrase=passwgpg)
    else: encrypted_data = mygpg.encrypt(unencrypted_string, username, sign=username)

    encrypted_string = str(encrypted_data)

    if verbose >= 3: print('ok: ', encrypted_data.ok)
    if verbose >= 3: print('status: ', encrypted_data.status)
    if verbose >= 3: print('stderr: ', encrypted_data.stderr)
    print("-" * 72)
    if verbose >= 1: print('encrypted_string: ', encrypted_string)
    print("-" * 72)

    if passwgpg != "": decrypted_data = mygpg.decrypt(encrypted_string, passphrase=passwgpg)
    else: decrypted_data = mygpg.decrypt(encrypted_string)

    if verbose >= 3: print('ok: ', decrypted_data.ok)
    if verbose >= 3: print('status: ', decrypted_data.status)
    if verbose >= 3: print('stderr: ', decrypted_data.stderr)
    print("-" * 72)
    if verbose >= 1: print('decrypted string: ', decrypted_data.data.decode("utf-8"))
    print("-" * 72)

    if not decrypted_data.username: print("ERROR: Signature could not be verified!")
    if verbose >= 1: print('verifyed by: ', decrypted_data.username)

# encriptado: OK, firmado: ?
def test5(mygnupghome, username, passwgpg, verbose):
    mygpg = gnupg.GPG(gnupghome=mygnupghome)
    encrypted_string = b"""-----BEGIN PGP MESSAGE-----

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
q1JPhEcoq+Wojk3O8GYnef7o9lQVmig=
=LyFf
-----END PGP MESSAGE-----"""

    if verbose >= 1: print('encrypted_string: ', encrypted_string)
    print("-" * 72)

    if passwgpg != "": decrypted_data = mygpg.decrypt(encrypted_string, passphrase=passwgpg)
    else: decrypted_data = mygpg.decrypt(encrypted_string)

    if verbose >= 3: print('ok: ', decrypted_data.ok)
    if verbose >= 3: print('status: ', decrypted_data.status)
    if verbose >= 3: print('stderr: ', decrypted_data.stderr)
    print("-" * 72)
    decrypted_data_ok = quopri.decodestring(decrypted_data.data.decode("utf-8")).decode("utf-8")
    if verbose >= 1: print('decrypted string: ', decrypted_data_ok)
    print("-" * 72)

    if verbose >= 1: print('sig block: ', utils.get_sig_blk(decrypted_data_ok))
    print("-" * 72)

    if verbose >= 1: print('msg block: ', utils.get_msg_blk(decrypted_data_ok))
    print("-" * 72)

    # if not decrypted_data.username: print("ERROR: Signature could not be verified!")
    # if verbose >= 1: print('verifyed by: ', decrypted_data.username)
