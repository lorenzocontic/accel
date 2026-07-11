from utils import hash_text
from constants import ALIAS_LENGTH


def generate(url):

    return hash_text(url)[:ALIAS_LENGTH]
