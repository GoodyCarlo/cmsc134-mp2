# Args parsing
import argparse
import pathlib

passParserParent = argparse.ArgumentParser(add_help=False)
passParserParent.add_argument(
    "-p",
    "--password",
    default="password",
    type=str,
    help="Enters a passphrase used in the encryption/decryption process",
)

msgPathParserParent = argparse.ArgumentParser(add_help=False)
msgPathParserParent.add_argument(
    "-mpath",
    "--message-path",
    default=pathlib.WindowsPath("msg.json"),
    type=pathlib.Path,
    help="Path to msg.json",
)

pTextParserParent = argparse.ArgumentParser(add_help=False)
pTextParserParent.add_argument(
    "message", type=str, help="Enter a message to be encrypted/decrypted"
)

keyParserParent = argparse.ArgumentParser(add_help=False)
keyParserParent.add_argument(
    "-c", "--create-key", action="store_true", help="Creates a new key"
)

SParserParent = argparse.ArgumentParser(add_help=False)
SParserParent.add_argument(
    "-ssk",
    "--signing-sk",
    default=pathlib.WindowsPath("keys/signing_sk.pem"),
    type=pathlib.Path,
    help="Path to signing_sk.pem",
)
SParserParent.add_argument(
    "-epk",
    "--encryption-pk",
    default=pathlib.WindowsPath("keys/encryption_pk.pem"),
    type=pathlib.Path,
    help="Path to encryption_pk.pem",
)

RParserParent = argparse.ArgumentParser(add_help=False)
RParserParent.add_argument(
    "-spk",
    "--signing-pk",
    default=pathlib.WindowsPath("keys/signing_pk.pem"),
    type=pathlib.Path,
    help="Path to signing_pk.pem",
)
RParserParent.add_argument(
    "-esk",
    "--encryption-sk",
    default=pathlib.WindowsPath("keys/encryption_sk.pem"),
    type=pathlib.Path,
    help="Path to encryption_sk.pem",
)


# For mainParser
mainParser = argparse.ArgumentParser(
    parents=[
        SParserParent,
        RParserParent,
        passParserParent,
        msgPathParserParent,
        keyParserParent,
        pTextParserParent,
    ]
)

# For create_key.py
createParser = argparse.ArgumentParser(
    parents=[SParserParent, RParserParent, passParserParent]
)

# For sender.py
senderParser = argparse.ArgumentParser(
    parents=[
        SParserParent,
        passParserParent,
        msgPathParserParent,
        keyParserParent,
        pTextParserParent,
    ]
)

# For receiver.py
receiverParser = argparse.ArgumentParser(
    parents=[RParserParent, passParserParent, msgPathParserParent]
)
