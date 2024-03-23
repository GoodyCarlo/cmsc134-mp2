# Args parsing
import argparse
import pathlib

SParserParent = argparse.ArgumentParser(add_help=False)
SParserParent.add_argument("-ssk", "--signingsk", default=pathlib.WindowsPath('keys/signing_sk.pem') , type=pathlib.Path, help="Path to signing_sk.pem")
SParserParent.add_argument("-epk", "--encryptionpk", default=pathlib.WindowsPath('keys/encryption_pk.pem') , type=pathlib.Path, help="Path to encryption_pk.pem")

RParserParent = argparse.ArgumentParser(add_help=False)
RParserParent.add_argument("-spk", "--signingpk", default=pathlib.WindowsPath('keys/signing_pk.pem') , type=pathlib.Path, help="Path to signing_pk.pem")
RParserParent.add_argument("-esk", "--encryptionsk", default=pathlib.WindowsPath('keys/encryption_sk.pem') , type=pathlib.Path, help="Path to encryption_sk.pem")



# For create_key.py
createParser = argparse.ArgumentParser(parents=[SParserParent, RParserParent])

# For sender.py
senderParser = argparse.ArgumentParser(parents=[SParserParent])
senderParser.add_argument("-c", "--createkey", action='store_true', help="Creates a new key")
senderParser.add_argument("-m", "--message", type=str, help="Enter a message to be encrypted/decrypted")

# For receiver.py
receiverParser = argparse.ArgumentParser(parents=[RParserParent])
receiverParser.add_argument("-mpath", "--messagepath", default=pathlib.WindowsPath('msg.json') ,type=pathlib.Path, help="Path to msg.json")

# For mainParser
mainParser = argparse.ArgumentParser(parents=[createParser])
mainParser.add_argument("-c", "--createkey", action='store_true', help="Creates a new key")