#!/usr/bin/python3

import configparser

config = configparser.ConfigParser()
config.read('config')
username1 = config['reddit']['username']
password1 = config['reddit']['password']
username2 = config['local database']['username']
password2 = config['local database']['password']
print(username1);
print(password1);
print(username2);
print(password2);
