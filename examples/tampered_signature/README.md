## This test changes the first character of the message's ciphertext.

### To check the original message:

```bash
python receiver.py -mpath examples/tampered_signature/msg_original.json
```

Expected output is: "The signature of this message has been tampered with"

### To check the tampered message:

```bash
python receiver.py -mpath examples/tampered_signature/msg_tampered_signature.json
```

Expected output is: "Invalid signature"
