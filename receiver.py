import json
from pathlib import Path

from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pss


def verify(pk, text, signature):
    # Hash is mandatory for this implementation of PSS: https://pycryptodome.readthedocs.io/en/latest/src/signature/pkcs1_pss.html
    hashed_text = SHA256.new(text)
    verifier = pss.new(pk)
    verifier.verify(hashed_text, signature)


def decrypt(sk, ciphertext):
    cipher = PKCS1_OAEP.new(sk)
    text = cipher.decrypt(ciphertext)
    return text


def main(
    spkPATH=Path("keys/signing_pk.pem"),
    eskPATH=Path("keys/encryption_sk.pem"),
    messagePath=Path("msg.json"),
    pwd="password",
):

    # import keys
    verify_public_key = RSA.importKey(
        open(spkPATH).read(),
    )
    decrypt_private_key = RSA.importKey(
        open(eskPATH).read(),
        passphrase=pwd,
    )

    # read message and store from dictionary
    with open(messagePath, "r") as f:
        hex_message = json.load(f)

        # convert ciphertext and signature back to bitstring
        ciphertext = bytes.fromhex(hex_message["ciphertext"])
        signature = bytes.fromhex(hex_message["signature"])

    try:
        verify(verify_public_key, ciphertext, signature)
        try:
            plaintext = decrypt(decrypt_private_key, ciphertext)
            print(plaintext.decode())
        except ValueError:
            print("Invalid ciphertext")
    except ValueError:
        print("Invalid signature")


if __name__ == "__main__":
    from args import receiverParser

    args = receiverParser.parse_args()

    main(args.signing_pk, args.encryption_sk, args.message_path, args.password)
