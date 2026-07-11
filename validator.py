from constants import SUPPORTED_PROTOCOLS


def valid(url):

    return url.startswith(
        SUPPORTED_PROTOCOLS
    )
