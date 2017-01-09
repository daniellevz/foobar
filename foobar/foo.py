import postgresql, requests
from .config import config

def foo():
    """ This is a docstring: returns \`foo\`"""
    return config['db'].prepare("SELECT 'foo'").first()
