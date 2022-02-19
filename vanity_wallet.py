#!/usr/bin/env
from bitsv import Key, PrivateKey

for _ in range(1000):
	my_key = PrivateKey(network='test')
	print(my_key.address)
	print(my_key.to_hex())
	sleep (3)
