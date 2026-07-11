import hashlib


def hash_text(text):

    return hashlib.sha1(
        text.encode()
    ).hexdigest()
