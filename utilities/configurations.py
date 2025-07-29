import requests
import configparser
import json

def getconfig(path):
    config = configparser.ConfigParser()
    config.read(path)
    return config