import leancloud

app_id = 'xKpYPGEr9FR5XQIxd51IHi9Q-gzGzoHsz'
app_key = 'DCqkxJdi260n1ik8vTM0U75l'


def lc_depth():
    leancloud.init(app_id, app_key)
    C = leancloud.Object.extend('Depth')
    obj = C()
    return obj


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
    return


if __name__ == "__main__":
    main()
