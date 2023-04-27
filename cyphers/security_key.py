def enter_key():
    key = int(input("Enter your security number:\n"))
    keys = []
    while key > 0:
        keys.append(key % 256)
        key //= 256
    if len(keys) == 0:
        keys.append(0)
    return keys
