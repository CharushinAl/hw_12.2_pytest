def get_val(collection, key, default='git'):
    '''
    Функция возвращает значение словаря по заданному ключу,
    если ключ существует. В ином случае возвращает default.
    :param collection: dictionary
    :param key: key og dictionary
    :param default: return if key not exist
    :return: string
    '''
    return collection.get(key, default)
