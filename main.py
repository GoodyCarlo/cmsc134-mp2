# Main
import create_key
import receiver
import sender
from args import mainParser

args = mainParser.parse_args()

if args.create_key:
    create_key.main(
        args.encryption_pk,
        args.encryption_sk,
        args.signing_pk,
        args.signing_sk,
        args.password,
    )

sender.main(
    args.message,
    args.signing_sk,
    args.encryption_pk,
    args.message_path,
    args.password,
)

receiver.main(
    args.signing_pk,
    args.encryption_sk,
    args.message_path,
    args.password,
)
