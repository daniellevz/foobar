import postgresql, requests
from .config import config

def bar():
    """ This is a docstring: returns \`foo\`"""
    return config['db'].prepare("SELECT 'bar'").first()
