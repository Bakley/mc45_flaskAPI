import os


class Development:
    DEBUG = True
    TESTING = False
    DATABASE_URI='postgresql+psycopg2://postgres:new_password@localhost/mc45'

class Testing:
    DEBUG = True
    TESTING = True
    TEST_DATABASE_URI='postgresql+psycopg2://postgres:new_password@localhost/mc45_test'
  


app_config = {
    'development': Development
}
