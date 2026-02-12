import json
from .EnterpriseManagementException import EnterpriseManagementException
from .EnterpriseRequest import EnterpriseRequest

class EnterpriseManager:
    def __init__(self):
        pass

    def ValidateCIF( self, CiF ):
        dicc = {
            0:"J",
            1:"A",
            2:"B",
            3:"C",
            4:"D",
            5:"E",
            6:"F",
            7:"G",
            8:"H",
            9:"I",
        }
        pos_central = CiF[1:-1]
        suma_pares = 0
        suma_impares = 0
        digito_impar = 0
        suma_total = 0
        unidad = 0
        digito_base = 0
        cc_letra = ""
        for i in range(len(pos_central)):
            if i%2 != 0:
                suma_pares += int(pos_central[i])
            elif i%2 == 0:
                digito_impar = int(pos_central[i])*2
                if digito_impar>9:
                    digito_impar = int(str(digito_impar)[0]) + int(str(digito_impar)[1])
                suma_impares += digito_impar
        suma_total = suma_pares + suma_impares
        unidad = int(str(suma_total)[-1])
        if unidad == 0:
            digito_base = 0
        else:
            digito_base = 10 - unidad
        if CiF[0] in ["A","B","E","H"]:
            return int(CiF[-1]) == digito_base
        if CiF[0] in ["K","P","Q","S"]:
            cc_letra = dicc[digito_base]
            return CiF[-1] == cc_letra
        return False




        return True

    def ReadproductcodefromJSON( self, fi ):

        try:
            with open(fi,encoding="UTF-8") as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise EnterpriseManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise EnterpriseManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            T_CIF = DATA["cif"]
            T_PHONE = DATA["phone"]
            E_NAME = DATA["enterprise_name"]
            req = EnterpriseRequest(T_CIF, T_PHONE,E_NAME)
        except KeyError as e:
            raise EnterpriseManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.ValidateCIF(T_CIF) :
            print(self.ValidateCIF(T_CIF))
            raise EnterpriseManagementException("Invalid FROM IBAN")
        return req