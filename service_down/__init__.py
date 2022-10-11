from service_down import settings

if not settings.DEBUG:
    import pymysql

    pymysql.install_as_MySQLdb()