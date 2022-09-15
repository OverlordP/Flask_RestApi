class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'eduardo32000'
    MYSQL_DB = 'bibliotecas'


config = {
    'development': DevelopmentConfig
}