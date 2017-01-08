from .app import app
from .config import config

app.run(config['app_host'], config['app_port'])

