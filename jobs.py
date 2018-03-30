import api_leancloud as lc
import api_binance as bn
from datetime import datetime
import time


def ETHUSDT():
    symbol = 'ETHUSDT'
    # interval = ('1m','3m','5m','15m','30m','1h','2h','4h','6h','8h','12h','1d','3d','1w','1M')
    interval = ('1m','5m','30m','4h','1d','1w')
    data = {}
    try:
        # add timestamp
        data['ts_start'] = int(time.time())
        # get depth data
        data['depth'] = bn.get_depth(symbol=symbol,limit=1000)
        # get kline data
        for i in interval:
            data['kline_'+i] = bn.get_current_kline(symbol=symbol,interval=i)
        # add finish timestamp & calculate time span
        data['ts_finish'] = int(time.time())
        data['ts_span'] = data['ts_finish'] - data['ts_start']
        # save data to leanCloud
        lc.save_to_cloud(tableName=symbol, dataObj=data)
        print('%s %s data uploaded' % (datetime.now(), symbol))
    except Exception as e:
        print(e)
        print('%s %s data upload failed' % (datetime.now(), symbol))
        pass
    return


def main():
    ETHUSDT()
    return


if __name__ == "__main__":
    main()
