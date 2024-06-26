from pathlib import Path
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
        prot_params={"iteration_count": 210000},
    )

    return public, private


def main(
    epkPATH=Path("keys/encryption_pk.pem"),
    eskPATH=Path("keys/encryption_sk.pem"),
    spkPATH=Path("keys/signing_pk.pem"),
    sskPATH=Path("keys/signing_sk.pem"),
    pwd="password",
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
    main(
        args.encryption_pk,
        args.encryption_sk,
        args.signing_pk,
        args.signing_sk,
        args.password,
    )
