# import libaries

from Crypto.Cipher import PKCS1_OAEP

from Crypto.PublicKey import RSA


def generate_keypair():
    mykey = RSA.generate(
        3072
    )  # TODO: Consider using a 2048-bit key just cuz that's what everyone does

    pwd = "password"

    public = mykey.public_key().export_key()

    private = mykey.export_key(
        passphrase=pwd,
        pkcs=8,
        protection="PBKDF2WithHMAC-SHA512AndAES256-CBC",
        prot_params={"iteration_count": 131072},
    )

    return public, private


if __name__ == "__main__":
    public, private = generate_keypair()
    with open("pk.pem", "wb") as f:
        f.write(public)

    with open("sk.pem", "wb") as f:
        f.write(private)
