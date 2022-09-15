class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'secret'
    MYSQL_DB = 'secret'


config = {
    'development': DevelopmentConfig
}