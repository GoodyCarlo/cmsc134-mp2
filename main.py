# Main
import create_key
import receiver
import sender
from args import mainParser

args = mainParser.parse_args()

if args.createkey:
    create_key.main(
        args.encryptionpk,
        args.encryptionsk,
        args.signingpk,
        args.signingsk,
        args.pwd,
    )

sender.main(
    args.message,
    args.signingsk,
    args.encryptionpk,
    args.messagepath,
    args.pwd,
)

receiver.main(
    args.signingpk,
    args.encryptionsk,
    args.messagepath,
    args.pwd,
)
