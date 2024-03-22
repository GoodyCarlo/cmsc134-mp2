# Args parsing
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("message", type=str, help="Enter a message to be encrypted/decrypted")
parser.add_argument("-c", "--createkey", action='store_true', help="Creates a new key")
args = parser.parse_args()

message = args.message

# Main
import create_key, receiver, sender
if args.createkey:
    create_key.main()
sender.main(message)
receiver.main()