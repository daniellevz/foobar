import postgresql

config = dict(
    app_host    = '0.0.0.0',
    app_port    = 80,
    db_user     = 'postgres',
    db_host     = 'localhost',
    db_password = '1234',
)

config['db'] = postgresql.open(user=config['db_user'], host=config['db_host'], password=config['db_password'])
