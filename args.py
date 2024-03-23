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
createParser = argparse.ArgumentParser(parents=[SParserParent, RParserParent], add_help=False)
createParser.add_argument('-h', '--help', action='help', help='Show this help message and exit')
cpArgs = createParser.parse_args()

# For sender.py
senderParser = argparse.ArgumentParser(parents=[SParserParent], add_help=False)
senderParser.add_argument('-h', '--help', action='help', help='Show this help message and exit')
senderParser.add_argument("-c", "--createkey", action='store_true', help="Creates a new key")
senderParser.add_argument("-m", "--message", type=str, help="Enter a message to be encrypted/decrypted")
spArgs = senderParser.parse_args()

# For receiver.py
receiverParser = argparse.ArgumentParser(parents=[RParserParent], add_help=False)
receiverParser.add_argument('-h', '--help', action='help', help='Show this help message and exit')
receiverParser.add_argument("-mpath", "--messagepath", default=pathlib.WindowsPath('msg.json') ,type=pathlib.Path, help="Path to msg.json")
rpArgs = receiverParser.parse_args()

# For mainParser
mainParser = argparse.ArgumentParser(parents=[createParser], add_help=False)
mainParser.add_argument('-h', '--help', action='help', help='Show this help message and exit')
mainParser.add_argument("-c", "--createkey", action='store_true', help="Creates a new key")
mpArgs = mainParser.parse_args()