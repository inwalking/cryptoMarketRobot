import requests
from datetime import datetime

"""
LIMITS
https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md

- The /api/v1/exchangeInfo rateLimits array contains objects related to the exchange's REQUESTS and ORDER rate limits.
- A 429 will be returned when either rather limit is violated.
- Each route has a weight which determines for the number of requests each endpoint counts for. Heavier endpoints and endpoints that do operations on multiple symbols will have a heavier weight.
- When a 429 is recieved, it's your obligation as an API to back off and not spam the API.
- Repeatedly violating rate limits and/or failing to back off after receiving 429s will result in an automated IP ban (http status 418).
- IP bans are tracked and scale in duration for repeat offenders, from 2 minutes to 3 days.

"""


def get_depth(symbol='ETHUSDT', limit=100):
    """ get coin depth data
    :param symbol: such as 'ETHUSDT'
    :param limit: 5, 10, 20, 50, 100 - weight 1
                500 - weight 5
                1000 - weight 10
    :return: json or error code
    """
    p = {'symbol': symbol, 'limit': limit}
    r = requests.get('https://api.binance.com/api/v1/depth', params=p)
    if 200 == r.status_code:
        return r.json()
    else:
        print('%s failed on /api/v1/depth' % datetime.now())
        return r.status_code


def get_current_kline(symbol='ETHUSDT', interval='1m', limit=100):
    """ get current kline data (weight:1)
    :param symbol: such as 'ETHUSDT'
    :param interval: such as 1m,3m,5m,15m,30m,1h,2h,4h,6h,8h,12h,1d,3d,1w,1M
    :param limit: default 100
    :return: json or error code
    """
    p = {'symbol': symbol, 'interval': interval, 'limit': limit}
    r = requests.get('https://api.binance.com/api/v1/klines', params=p)
    if 200 == r.status_code:
        return r.json()
    else:
        print('%s failed on /api/v1/klines' % datetime.now())
        return r.status_code


def main():
    # get_depth()
    a = get_current_kline()
    print()
    return


if __name__ == "__main__":
    main()
