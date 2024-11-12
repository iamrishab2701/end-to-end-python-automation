import configparser

import mysql
import paramiko
from mysql.connector import Error
from paramiko import sftp


def get_config():
    config = configparser.ConfigParser()
    config.read('/Users/rishab/PycharmProjects/end-to-end-python-automation/utilities/properties.ini')
    return config


def get_github_token():
    return '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'


def get_github_email():
    return 'singhrishab166@gmail.com'


connect_config = {
    'host': get_config()['SQL']['host'],
    'database': get_config()['SQL']['database'],
    'user': get_config()['SQL']['user'],
    'password': get_config()['SQL']['password']
}


def get_mysql_connection():
    try:
        connection = mysql.connector.connect(**connect_config)
        if connection.is_connected():
            print("Connection Successful")
            return connection
    except Error as e:
        print(e)


def get_query(query):
    mysql_connection = get_mysql_connection()
    mysql_cursor = mysql_connection.cursor()
    mysql_cursor.execute(query)
    first_row = mysql_cursor.fetchone()
    mysql_connection.close()
    return first_row