import sys
import parser
import config


def main():
    try:
        parser.parse(sys.argv[1:])
    except parser.ParsingError as inst:
        print("ParsingError:", inst)
        print("Use --help flag to see possible options")
        return 1
    if config.cypher == "auto decrypter":
        import cyphers.auto_decrypter as encryptor
    elif config.cypher == "caesar":
        import cyphers.caesar as encryptor
    elif config.cypher == "vigenere":
        import cyphers.vigenere as encryptor
    elif config.cypher == "vernam":
        import cyphers.vernam as encryptor
    elif config.cypher == "steganography":
        import cyphers.steganography as encryptor
    try:
        if config.args["encrypt"]:
            encryptor.encrypt(config.source_file, config.output_file, config.args["mode"])
        else:
            encryptor.decrypt(config.source_file, config.output_file, config.args["mode"])
    except cyphers.steganography.StenographyError as inst:
        print("Steganography error: ", inst)
        return 1
    print("Completed successfully, output file:", config.output_file)
    return 0


if __name__ == '__main__':
    main()
