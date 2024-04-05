This test changes the first character of the message's signature.

To check the original message:

python receiver.py -mpath examples/tampered_ciphertext/msg_original.json

Expected output is: "The ciphertext of this message has been tampered with"


To check the tampered message:

python receiver.py -mpath examples/tampered_ciphertext/msg_tampered_ciphertext.json

Expected output is: "Invalid signature"
