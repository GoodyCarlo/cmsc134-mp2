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


if __name__ == "__main__":
    public_encryption, private_encryption = generate_keypair(pwd="password")
    with open("keys/encryption_pk.pem", "wb") as f:
        f.write(public_encryption)
    with open("keys/encryption_sk.pem", "wb") as f:
        f.write(private_encryption)

    public_signing, private_signing = generate_keypair(pwd="password")
    with open("keys/signing_pk.pem", "wb") as f:
        f.write(public_signing)
    with open("keys/signing_sk.pem", "wb") as f:
        f.write(private_signing)
