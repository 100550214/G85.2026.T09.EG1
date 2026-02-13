"""importar clasees """
import string
from pathlib import Path
from uc3m_consulting import EnterpriseManager

#GLOBAL VARIABLES
letters = string.ascii_letters + string.punctuation + string.digits
shift = 3

#newtest

def encode(word):
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (letters.index(letter) + shift) % len(letters)
            encoded = encoded + letters[x]
    return encoded

def decode(word):
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (letters.index(letter) - shift) % len(letters)
            encoded = encoded + letters[x]
    return encoded

def get_test_path(filename):
    return os.path.join(TESTS_DIR, filename)


def main():
    BASE_DIR = Path(__file__).resolve().parent
    TESTS_DIR = BASE_DIR / "tests"
    mng = EnterpriseManager()
    res = mng.readproductcodefrom_json("test.json")
    str_res = res.__str__()
    print(str_res)
    encode_res = encode(str_res)
    print("Encoded Res "+ encode_res)
    decode_res = decode(encode_res)
    print("Decoded Res: " + decode_res)
    print("cif: " + res.ENTERPRISE_CIF)
    print("enterprise_name: " + res.ENTERPRISE_NAME)
    print("enterprise_phone: " + res.PHONE_NUMBER)

if __name__ == "__main__":
    main()
