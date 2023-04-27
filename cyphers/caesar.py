import cyphers.security_key


def reformat(symbol, key, first, last):
    size = ord(last) - ord(first) + 1
    key = (key % size + size) % size
    return str(chr(ord(first) + ((ord(symbol) - ord(first)) + key) % size))


def shift(symbol, key):
    if 'z' >= symbol >= 'a':
        return reformat(symbol, key, 'a', 'z')
    elif 'Z' >= symbol >= 'A':
        return reformat(symbol, key, 'A', 'Z')
    elif 'я' >= symbol >= 'а':
        return reformat(symbol, key, 'а', 'я')
    elif 'Я' >= symbol >= 'А':
        return reformat(symbol, key, 'А', 'Я')
    else:
        return symbol


def caesar(source, output, mode, key):
    if mode == "binary":
        with open(source, 'rb') as src:
            with open(output, 'wb') as out:
                arr = [((symbol + key + 256) % 256) for symbol in src.read()]
                out.write(bytearray(arr))
    else:
        with open(source, 'r') as src:
            with open(output, 'w') as out:
                encrypted = "".join([shift(symbol, key) for symbol in src.read()])
                out.write(encrypted)


def encrypt(source, output, mode):
    keys = cyphers.security_key.enter_key()
    caesar(source, output, mode, keys[0])


def decrypt(source, output, mode):
    keys = cyphers.security_key.enter_key()
    caesar(source, output, mode, -keys[0])
