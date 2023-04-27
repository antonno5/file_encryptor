import cyphers.security_key


def encrypt(source, output, mode):
    keys = cyphers.security_key.enter_key()
    with open(source, 'rb') as src:
        with open(output, 'wb') as out:
            arr = []
            index = 0
            for symbol in src.read():
                arr.append((symbol + keys[index]) % 256)
                index = (index + 1) % len(keys)
            out.write(bytearray(arr))


def decrypt(source, output, mode):
    keys = cyphers.security_key.enter_key()
    with open(source, 'rb') as src:
        with open(output, 'wb') as out:
            arr = []
            index = 0
            for symbol in src.read():
                arr.append((symbol - keys[index] + 256) % 256)
                index = (index + 1) % len(keys)
            out.write(bytearray(arr))