import cyphers.caesar
import operator


def decrypt(source, output, mode):
    key = 0
    with open(source, "r") as file:
        russian = [chr(symbol) for symbol in range(ord('а'), ord('я') + 1)]
        english = [chr(symbol) for symbol in range(ord('a'), ord('z') + 1)]
        cnt = dict.fromkeys(russian + english, 0)
        for symbol in file.read():
            if 'z' >= symbol >= 'a':
                cnt[symbol] += 1
            if 'Z' >= symbol >= 'A':
                cnt[symbol.lower()] += 1
            if 'я' >= symbol >= 'а':
                cnt[symbol] += 1
            if 'Я' >= symbol >= 'А':
                cnt[symbol.lower()] += 1
        letter = max(cnt.items(), key=operator.itemgetter(1))[0]
        if 'z' >= letter >= 'a':
            key = ord('e') - ord(letter)
        else:
            key = ord('о') - ord(letter)
        print("Expected key:", key)
    cyphers.caesar.caesar(source, output, "non_binary", key)
