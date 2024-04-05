## This test attempts to read an encrypted message with the wrong keypair

### To create the false keypairs:

```python
python create_key.py \
-ssk examples/wrong_keypair/keys/signing_sk.pem \
-epk examples/wrong_keypair/keys/encryption_pk.pem \
-spk examples/wrong_keypair/keys/signing_pk.pem \
-esk examples/wrong_keypair/keys/encryption_sk.pem
```

### To create the message:

```
python sender.py "I like CMSC134!" -mpath examples/wrong_keypair/msg.json
```

### To read the message with the wrong keypair

```python
python receiver.py \
-mpath examples/wrong_keypair/msg.json \
-spk examples/wrong_keypair/keys/signing_pk.pem \
-esk examples/wrong_keypair/keys/encryption_sk.pem
```

Expected output is: `Invalid signature`

### To read the message with the right keypair:

```python
python receiver.py -mpath examples/wrong_keypair/msg.json
```

Expected output is: `I like CMSC134!`

