# -*- coding: utf-8 -*-
# crack password of pdf using python

import pikedf
from tqdm import tqdm

passwords= [line.strip() for line in open("wordlist.txt")]

for password in tqdm(passwords, "Decryptinf PDF"):
    try:
        with pikepdf.open("sample.pdf", password=password) as pdf:
            print("\n [+] Password Found: ", password)
            break
    except pikepdf._qpdf.PasswordError as e:
        #wrong password, just continue in the loop
        continue

