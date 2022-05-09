from flask_sqlalchemy import SQLAlchemy 
import os
from os.path import abspath
from os.path import dirname
from os.path import join
from os.path import pardir
from dotenv import load_dotenv
from sqlalchemy.pool import QueuePool
from sqlalchemy.pool import StaticPool



dotenv_path = abspath(join(dirname(__file__), pardir, '.env'))
load_dotenv(dotenv_path)
os.getenv("ACCESS_KEY")

QA_ENVIRONMENT = 'qa'
DEV_ENVIRONMENT = 'dev'
PROD_ENVIRONMENT = 'prod'
TEST_ENVIRONMENT = 'test'
ENVIRONMENT = os.environ.get('Environment') or DEV_ENVIRONMENT
ENVIRONMENTS = [QA_ENVIRONMENT, DEV_ENVIRONMENT, PROD_ENVIRONMENT,TEST_ENVIRONMENT]
if ENVIRONMENT not in ENVIRONMENTS:
    raise Exception('The environment used is not properly named.')

APP_URL = os.environ.get('APP_URL', 'http://localhost:5000')

DB_CREDENTIALS = {
    'database': 'mydatabase',#os.environ.get('MYSQL_DATABASE'),
    'host': 'localhost',#os.environ.get('MYSQL_HOST'),
    'password': 'root',#os.environ.get('MYSQL_PASSWORD'),
 #   'port': os.environ.get('MYSQL_PORT'),
    'user': 'root'#os.environ.get('MYSQL_USER')
}
if ENVIRONMENT == TEST_ENVIRONMENT:
    DB_URL = "mysql://"
    POOL_CLASS = StaticPool
    CONNECT_ARGS = {'check_same_thread': False}
else:  
    DB_URL = (
    "mysql://{user}:{password}@{host}/{db}"
    .format(
        user=DB_CREDENTIALS.get('user'),
        password=DB_CREDENTIALS.get('password'),
        host=DB_CREDENTIALS.get('host'),
        db=DB_CREDENTIALS.get('database')
        ))
    POOL_CLASS = QueuePool
    POOL_SIZE = 15
    POOL_RECYCLE_MS = 3600  # Avoids connections going stale
    POOL_MAX_OVERFLOW = -1
    CONNECT_ARGS = {}

#mydatabase="mysql://{}:{}@{}/mydatabase".format(username,password,host)