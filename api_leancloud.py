import leancloud

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


def main():
    connection()
    return


if __name__ == "__main__":
    main()
