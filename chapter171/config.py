import configparser
from configparser import ConfigParser
config =ConfigParser()
file='config.ini'
config.read(file)

#print section student and client
print(config.sections())

#print student section with its parameters
print(list(config['student']))