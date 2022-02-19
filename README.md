# bsv_wallet

Used this website for reference:
https://austecon.github.io/bitsv/guide/keys.html

1. Check to see if you have the `bitsv` python library. 
`python -m pip list`

2. If you don't have it, install. `python -m pip install bitsv`

3. Make a file called `wallet.py`


4. Here is my example for creating a TestNet address. 
```
(.venv) rachael@Rachaels-MacBook-Pro wallet_fun % cat wallet.py 
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

Your wallet address will show. `mitiXLoYn6M4V81nyxzamLAyXJ1zPGJPHj`
This can be found on WhatsOnChain: https://test.whatsonchain.com/address/mitiXLoYn6M4V81nyxzamLAyXJ1zPGJPHj

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
