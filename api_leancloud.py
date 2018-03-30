import leancloud
import time

app_id = 'xKpYPGEr9FR5XQIxd51IHi9Q-gzGzoHsz'
app_key = 'DCqkxJdi260n1ik8vTM0U75l'


def connection():
    leancloud.init(app_id, app_key)
    Todo = leancloud.Object.extend('Todo')
    todo = Todo()
    todo.set('title', '工程师周会')
    todo.set('content', '每周工程师会议，周一下午2点')
    todo.set('location', '会议室')  # 增加一个字段
    todo.save()
    return


def save_to_cloud(tableName='ETHUSDT', dataObj=None):
    """ save date to leancloud
    :param tableName: cloud table name
    :param dataObj: data dict
    :return: None
    """
    leancloud.init(app_id, app_key)
    T = leancloud.Object.extend(tableName)
    t = T()
    for key, item in dataObj.items():
        t.set(key, item)
    t.save()
    return


def fetch_from_cloud(tableName='ETHUSDT', itemNum=100, timeEnd=int(time.time()), interval=60):
    """
    :param tableName: cloud table name
    :param itemNum: total number of fetched items
    :param timeEnd: fetch the item before limitTime
    :param interval: timestamp intervals of each item
    :return: leanCloud obj list
    """
    queryLimit = 20
    timeHock = timeEnd
    remainNum = itemNum

    leancloud.init(app_id, app_key)
    T = leancloud.Object.extend(tableName)
    q1 = T.query
    q2 = T.query
    query = T.query
    query.limit(queryLimit)

    result = []
    while remainNum > 0:
        if remainNum < queryLimit:
            queryLimit = remainNum
        q1.greater_than_or_equal_to('ts_finish', timeHock - queryLimit * interval)
        q2.less_than('ts_finish', timeHock)
        query = leancloud.Query.and_(q1, q2)
        result += query.find()  # fetch data
        timeHock -= queryLimit * interval
        remainNum -= queryLimit
        print('Fetching Data: %s / %s' % (itemNum - remainNum, itemNum))

    return result


def main():
    connection()
    a = fetch_from_cloud()
    return


if __name__ == "__main__":
    main()
