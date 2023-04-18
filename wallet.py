#!/usr/bin/env python3
from bitsv import Key, PrivateKey
network = "main"
my_key_test = PrivateKey(network=network)
print(my_key_test.address, file=open('bsv_public_address.txt','w')),
#https://austecon.github.io/bitsv/guide/keys.html#wif
#Wif is more common for your output of your private key
print(my_key_test.to_wif(), file=open('bsv_private_key.txt','a'))

#https://austecon.github.io/bitsv/guide/keys.html#hex
#This is the website to the bitsv libary which creates the wallets and keys. Most don't use HEX but uncomment line 10 if you want hex.
#print(my_key_test.to_hex())
