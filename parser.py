import config


class ParsingError(Exception):
    pass


def parse(argv):
    index = 0
    while index < len(argv):
        if argv[index] == "--help":
            print('''-b, -B, --binary: Переводит алгоритмы в бинарный режим, то есть будут шифроваться не только буквы, но
и все остальные символы (все алгоритмы, кроме шифра Цезаря не чувствительны к этому флагу)

-c, -C, --cypher: Установить шифр, который будет применяться по кодовому слову, если не указан,
то будет использоваться шифр Цезаря

-d, -D, --decrypt: Шифровать исходный файл

-e, -E, --encrypt: Расшифровать исходный файл, по умолчанию включен

--help: Вывести всю документацию по программе

-o, -O, --output: Установить выходной файл, если этот флаг не указан, то будет создан файл с
расширением .encrypted при шифровке и .decrypted при расшифровке в той же директории, что и исходный
файл и с таким же именем

-s, -S, --source: Установить путь к файлу с исходным текстом(обязательный флаг)''')
            exit()
        elif argv[index] == "-e" or argv[index] == "-E" or argv[index] == "--encrypt":
            config.args["encrypt"] = True
            index += 1
            continue
        elif argv[index] == "-d" or argv[index] == "-D" or argv[index] == "--decrypt":
            config.args["encrypt"] = False
            index += 1
            continue
        elif argv[index] == "-b" or argv[index] == "-B" or argv[index] == "--binary":
            config.args["mode"] = "binary"
            index += 1
            continue
        elif index == len(argv) - 1:
            raise ParsingError("incorrect options usage")
        elif argv[index] == "-s" or argv[index] == "-S" or argv[index] == "--source":
            config.source_file = argv[index + 1]
        elif argv[index] == "-c" or argv[index] == "-C" or argv[index] == "--cypher":
            if argv[index + 1] == "caesar" or argv[index + 1] == "vigenere" or argv[index + 1] == "vernam" or argv[index + 1] == "steganography":
                config.cypher = argv[index + 1]
            elif argv[index + 1] == "auto_decrypter":
                config.cypher = "auto decrypter"
                config.args["encrypt"] = False
            else:
                raise ParsingError("incorrect cypher " + argv[index + 1])
        elif argv[index] == "-o" or argv[index] == "-O" or argv[index] == "--output":
            config.output_file = argv[index + 1]
        else:
            raise ParsingError("incorrect option " + argv[index])
        index += 2

    if config.source_file == "":
        raise ParsingError("you should set source file")
    if config.output_file == "":
        if config.args["encrypt"]:
            config.output_file = config.source_file + ".encrypted"
        else:
            config.output_file = config.source_file + ".decrypted"
