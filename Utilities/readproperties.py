import configparser
# import os
config=configparser.RawConfigParser()
# config_path = os.path.join(os.path.dirname("C:/Users/train\PycharmProjects/NopCommerceApp/Configurations/Config.ini"), 'Config.ini')
config.read("C:/Users/train/PycharmProjects/NopCommerceApp/Configurations/Config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationurl():
        url=config.get('common info','baseurl')
        return url
    @staticmethod
    def getusername():
        username=config.get('common info','Username')
        return username
    @staticmethod
    def getpassword():
        password=config.get('common info','Password')
        return password

