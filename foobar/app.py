import flask
from .config import config
from .foo import foo
from .bar import bar

app = flask.Flask(__name__)

@app.route('/foo')
def get_foo():
    return foo()


@app.route('/bar')
def get_bar():
    return bar()

if __name__ == '__main__':
    app.run(config['app_host'], config['app_port'])
