from base64 import b64decode
import os
import keyring

f=open(os.path.expanduser("~/ralsina_ring.cfg"),"w+")
f.write(b64decode('W2tleXJpbmctc2V0dGluZ10KY3J5cHRlZC1wYXNzd29yZCA9IGNhdlB5OHpEaXJqVlEKW3B5YXJdCnJhbHNpbmEgPSBZUCtHQThsaC9VTUtnQzFEZC93PQo='))
f.close()

class Inofensivo(keyring.backend.CryptedFileKeyring):
    def filename(self):
        return "ralsina_ring.cfg"

keyring.set_keyring(Inofensivo())
print keyring.get_password('pyar','ralsina')
os.unlink(os.path.expanduser("~/ralsina_ring.cfg"))
