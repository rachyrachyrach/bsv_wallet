# Wallet Address Fun with bitsv. 

Used [Austecon bitsv guide](https://austecon.github.io/bitsv/guide/keys.html)


This small python script will create you a BitcoinSV wallet. You can make wallet addresses on the TestNet and MainNet by altering the script.

1. Check to see if you have the `bitsv` python library. 
`python -m pip list`

2. If you don't have it, install. `python -m pip install bitsv`

3. Make a file called `wallet.py`


4. Add this script in your file for creating a TestNet address. 
```
#!/usr/bin/env python3
from bitsv import Key, PrivateKey
network = "test"
my_key_test = PrivateKey(network=network)
print(my_key_test.address)
```
Run your file `python wallet.py`

You can run this several times to create many wallets! Here is an example: 
```
(.venv) rachael@Rachaels-MacBook-Pro wallet_fun % python wallet.py 
n17jkq8fFrqzy8o6C2kEKxZKkFg5HBS55y
(.venv) rachael@Rachaels-MacBook-Pro wallet_fun % python wallet.py
mkdazBzq6qny3dre1Tp2fK688jwfXtbEpi
(.venv) rachael@Rachaels-MacBook-Pro wallet_fun % python wallet.py
n4XkA4sjdfaXawEs31xqyjVWsJGfdAXKWZ
(.venv) rachael@Rachaels-MacBook-Pro wallet_fun % python wallet.py
mqwhizhcYszYXYcyRAhwbHRNUMJVqJ7ALw
(.venv) rachael@Rachaels-MacBook-Pro wallet_fun % python wallet.py
n1aokkjJ3Gv7pPc19AJwTAqvyzpv46a6ST
(.venv) rachael@Rachaels-MacBook-Pro wallet_fun % python wallet.py
mitiXLoYn6M4V81nyxzamLAyXJ1zPGJPHj
```
Here are my wallet addresses: 
`n1aokkjJ3Gv7pPc19AJwTAqvyzpv46a6ST`

`mqwhizhcYszYXYcyRAhwbHRNUMJVqJ7ALw`

`n4XkA4sjdfaXawEs31xqyjVWsJGfdAXKWZ`

`mkdazBzq6qny3dre1Tp2fK688jwfXtbEpi`

`n17jkq8fFrqzy8o6C2kEKxZKkFg5HBS55y`

`mitiXLoYn6M4V81nyxzamLAyXJ1zPGJPHj`

Search for your address on WhatsOnChain: https://test.whatsonchain.com/address/mitiXLoYn6M4V81nyxzamLAyXJ1zPGJPHj

Make a MainNet wallet address. Change `network = "test"` to `network = "main"`

```
#!/usr/bin/env python3
from bitsv import Key, PrivateKey
network = "main"
my_key_test = PrivateKey(network=network)
print(my_key_test.address)
```
https://whatsonchain.com/address/1LszG4TWQ8K38Ag1ZTomz3XCt1teZKmz9Y

MainNet address: 1LszG4TWQ8K38Ag1ZTomz3XCt1teZKmz9Y


File vanity_wallet.py was written to try to get a certain word in the wallet address. This is a python script that runs in a loop.  It also displays your private key. 


```
#!/usr/bin/env
from bitsv import Key, PrivateKey
from time import sleep

for _ in range(1000):
	my_key = PrivateKey(network='test')
	print(my_key.address)
	print(my_key.to_hex())
	sleep(3)
```

The line `print(my_key.to_hex())` shows your private key.  Remove this line if you don't want your private key to display. 
