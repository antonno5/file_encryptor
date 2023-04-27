class StenographyError(Exception):
    pass


def encrypt(source_file, output_file, mode):
    text_file = input("Enter path to file with your text:\n").strip()
    text = list()
    with open(text_file, "rb") as file:
        for symbol in file.read():
            text.append(symbol)
    buffer = list()
    src = list()
    with open(source_file, "rb") as file:
        string = file.read()
        for symbol in string[:512]:
            buffer.append(symbol)
        for symbol in string[512:]:
            src.append(symbol)
    if len(src) < len(text) * 8 + 1:
        raise StenographyError("your text is too large for this picture")
    arr = list()
    index = 0
    for byte in text:
        for bit in range(8):
            info = (byte >> bit) & 1
            printed = (src[index] // 4 * 4) + info
            arr.append(printed)
            index += 1
    arr.append(src[index] | 2)
    for byte in src[index + 1:]:
        arr.append(byte)
    with open(output_file, "wb") as file:
        file.write(bytearray(buffer))
        file.write(bytearray(arr))


def decrypt(source_file, output_file, mode):
    buffer = list()
    src = list()
    with open(source_file, "rb") as file:
        string = file.read()
        for symbol in string[:512]:
            buffer.append(symbol)
        for symbol in string[512:]:
            src.append(symbol)
    text = list()
    index = 0
    while True:
        if (src[index] & 2) != 0:
            break
        text.append(0)
        for bit in range(8):
            text[index // 8] += ((src[index] & 1) << bit)
            index += 1
    with open(output_file, "wb") as file:
        file.write(bytearray(text))
