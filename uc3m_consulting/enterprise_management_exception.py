"""importar clases """
from pylint.utils.pragma_parser import MESSAGE_KEYWORDS


class EnterpriseManagementException(Exception):
    def __init__(self, message):
        self.__MESSAGE = message
        super().__init__(self.MESSAGE)

    @property
    def MESSAGE(self):
        return self.__MESSAGE

    @MESSAGE.setter
    def MESSAGE(self, value):
        self.__MESSAGE = value
