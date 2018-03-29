from hashlib import sha256
import hmac
import requests
import simplejson
import api_leancloud



queryString = \
    'symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559'
secretKey = 'NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j'

h = hmac.new(secretKey.encode(), queryString.encode(), digestmod=sha256)
print(h.hexdigest())

# r = requests.get('https://api.binance.com/api/v1/time')
r = requests.get('https://api.binance.com/api/v1/ticker/24hr')
todo = api_leancloud.lc_depth()
todo.set('detail',r.json())
# todo.set('detail',1234)
todo.save()


# p_depth = {'symbol': 'ETHUSDT', 'limit': 100}
# r = requests.get('https://api.binance.com/api/v1/depth',params=p_depth)
#
# print(r.json()
#print(simplejson.dumps(r.json(), sort_keys=True, indent=4 * ' '))
