"""importar clases"""
import json
from datetime import datetime


class EnterpriseRequest:
    def __init__(self, cif, phone, ename):
        self.__ENTERPRISENAME = ename
        self.__CIF = cif
        self.__PHONE = phone
        justnow = datetime.utcnow()
        self.__TIMESTAMP = datetime.timestamp(justnow)

    def __str__(self):
        return "Enterprise:" + json.dumps(self.__dict__)

    @property
    def ENTERPRISE_CIF(self):
        return self.__CIF
    @ENTERPRISE_CIF.setter
    def ENTERPRISE_CIF(self, value):
        self.__CIF = value

    @property
    def PHONE_NUMBER(self):
        return self.__PHONE
    @PHONE_NUMBER.setter
    def PHONE_NUMBER(self, value):
        self.__PHONE = value

    @property
    def ENTERPRISE_NAME(self):
        return self.__ENTERPRISENAME
    @ENTERPRISE_NAME.setter
    def ENTERPRISE_NAME(self, value):
        self.__ENTERPRISENAME = value
