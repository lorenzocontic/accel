from database import DATABASE


def save(alias, url):

    DATABASE[alias] = url


def resolve(alias):

    return DATABASE.get(alias)


def all_links():

    return DATABASE
