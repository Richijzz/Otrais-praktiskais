import os
import requests
import mysql.connector

from datetime import datetime
from configparser import ConfigParser

print("Configuration file test")

# Testing if configuration file exists on disk in the current working directory
print("----------")
print("Checking if config file exists -->")
assert os.path.isfile("config.ini") == True
print("OK")
print("----------")

# Opening the configuration file
config = ConfigParser()
config.read('config.ini')

# Checking if all nasa related config options are present in the config file
print("Checking if config has NASA related options -->")
assert config.has_option('nasa', 'api_key') == True
assert config.has_option('nasa', 'api_url') == True
print("OK")
print("----------")

# Checking if all MYSQL related config options are present in the config file
print("Checking if config has MYSQL related options -->")
assert config.has_option('mysql_config', 'mysql_host') == True
assert config.has_option('mysql_config', 'mysql_db') == True
assert config.has_option('mysql_config', 'mysql_user') == True
assert config.has_option('mysql_config', 'mysql_pass') == True
print("OK")
print("----------")

# Checking if possible to connect to nasa with the existing config options
print("Checking if it is possible to connect to NASA API with the given config options -->")
nasa_api_key = config.get('nasa', 'api_key')
nasa_api_url = config.get('nasa', 'api_url')
dt = datetime.now()
request_date = str(dt.year) + "-" + str(dt.month).zfill(2) + "-" + str(dt.day).zfill(2) 
r = requests.get(nasa_api_url + "rest/v1/feed?start_date=" + request_date + "&end_date=" + request_date + "&api_key=" + nasa_api_key)
assert r.status_code == 200
print("OK")
print("----------")

# Checking if possible to connect to MySQL with the existing config options
print("Checking if it is possible to connect to MYSQL with the given config options -->")
mysql_config_mysql_host = config.get('mysql_config', 'mysql_host')
mysql_config_mysql_db = config.get('mysql_config', 'mysql_db')
mysql_config_mysql_user = config.get('mysql_config', 'mysql_user')
mysql_config_mysql_pass = config.get('mysql_config', 'mysql_pass')
connection = mysql.connector.connect(host=mysql_config_mysql_host, database=mysql_config_mysql_db, user=mysql_config_mysql_user, password=mysql_config_mysql_pass)
assert connection.is_connected() == True
print("OK")
print("----------")

# Checking if log config files exist for log config
print("Checking if DB migration component log config file exists log_migrate_db.yaml -->")
assert os.path.isfile("log_migrate_db.yaml") == True
print("OK")
print("----------")
print("Checking if asteroid worker component log config file exists log_worker.yaml -->")
assert os.path.isfile("log_worker.yaml") == True
print("OK")
print("----------")
print("Checking if log destination directory exists -->")
assert os.path.isdir("log") == True
print("OK")
print("----------")
print("Checking if migration source directory exists -->")
assert os.path.isdir("migrations") == True
print("OK")
print("----------")
print("Configuration file test DONE -> ALL OK")
print("----------------------------------------")