## This test checks if encrypting and signing the same plaintext gives different ciphertext

### To create the two messages:

```bash
python sender.py "Watch Suisei" -mpath examples/determinism_check/msg_1.json
python sender.py "Watch Suisei" -mpath examples/determinism_check/msg_2.json
```

### To check if two different texts have been generated:

```bash
cmp --silent examples/determinism_check/msg_1.json \
examples/determinism_check/msg_2.json || echo "files are different"
```

Expected output is: `files are different`
