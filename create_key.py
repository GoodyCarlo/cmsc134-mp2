import pathlib
from Crypto.PublicKey import RSA


def generate_keypair(pwd=None):
    mykey = RSA.generate(
        3072
    )  # TODO: Consider using a 2048-bit key just cuz that's what everyone does

    public = mykey.public_key().export_key()

    private = mykey.export_key(
        passphrase=pwd,
        pkcs=8,
        protection="PBKDF2WithHMAC-SHA512AndAES256-CBC",
        prot_params={"iteration_count": 131072},
    )

    return public, private


def main(
        epkPATH=pathlib.WindowsPath('keys/encryption_pk.pem'),
        eskPATH=pathlib.WindowsPath('keys/encryption_sk.pem'),
        spkPATH=pathlib.WindowsPath('keys/signing_pk.pem'),
        sskPATH=pathlib.WindowsPath('keys/signing_sk.pem'),
        pwd="password"
    ):
    public_encryption, private_encryption = generate_keypair(pwd=pwd)
    with open(epkPATH, "wb") as f:
        f.write(public_encryption)
    with open(eskPATH, "wb") as f:
        f.write(private_encryption)

    public_signing, private_signing = generate_keypair(pwd=pwd)
    with open(spkPATH, "wb") as f:
        f.write(public_signing)
    with open(sskPATH, "wb") as f:
        f.write(private_signing)


if __name__ == "__main__":
    from args import createParser
    args = createParser.parse_args()
    main(args.encryptionpk, args.encryptionsk, args.signingpk, args.signingsk, args.pwd)