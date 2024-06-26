# Args parsing
import argparse
from pathlib import Path

passwordParserParent = argparse.ArgumentParser(add_help=False)
passwordParserParent.add_argument(
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
    default=Path("msg.json"),
    type=Path,
    help="Path to msg.json",
)

plaintextParserParent = argparse.ArgumentParser(add_help=False)
plaintextParserParent.add_argument(
    "message", type=str, help="Enter a message to be encrypted/decrypted"
)

keyParserParent = argparse.ArgumentParser(add_help=False)
keyParserParent.add_argument(
    "-c", "--create-key", action="store_true", help="Creates a new key"
)

senderParserParent = argparse.ArgumentParser(add_help=False)
senderParserParent.add_argument(
    "-ssk",
    "--signing-sk",
    default=Path("keys/signing_sk.pem"),
    type=Path,
    help="Path to signature's private/signing key",
)
senderParserParent.add_argument(
    "-epk",
    "--encryption-pk",
    default=Path("keys/encryption_pk.pem"),
    type=Path,
    help="Path to message's public/encryption key",
)

receiverParserParent = argparse.ArgumentParser(add_help=False)
receiverParserParent.add_argument(
    "-spk",
    "--signing-pk",
    default=Path("keys/signing_pk.pem"),
    type=Path,
    help="Path to signature's public/validation key",
)
receiverParserParent.add_argument(
    "-esk",
    "--encryption-sk",
    default=Path("keys/encryption_sk.pem"),
    type=Path,
    help="Path to message's private/decryption key",
)


# For mainParser
mainParser = argparse.ArgumentParser(
    parents=[
        senderParserParent,
        receiverParserParent,
        passwordParserParent,
        msgPathParserParent,
        keyParserParent,
        plaintextParserParent,
    ],
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)

# For create_key.py
createParser = argparse.ArgumentParser(
    parents=[
        senderParserParent,
        receiverParserParent,
        passwordParserParent,
    ],
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)

# For sender.py
senderParser = argparse.ArgumentParser(
    parents=[
        senderParserParent,
        passwordParserParent,
        msgPathParserParent,
        plaintextParserParent,
    ],
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)

# For receiver.py
receiverParser = argparse.ArgumentParser(
    parents=[
        receiverParserParent,
        passwordParserParent,
        msgPathParserParent,
    ],
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
