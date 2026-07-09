import argparse

from utils import display_report, console
from analyzer import analyze_password, PasswordReport
from hash_utils import hash_password, identify_hash
from cracker import crack_hash

def main():
    parser = argparse.ArgumentParser(
        prog="password-auditor",
        description="Password Auditor - Security Tool"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    analyze_parser = subparsers.add_parser(
        "analyze",
        help="Analyze password strength"
    )

    analyze_parser.add_argument(
        "--password",
        required=True,
        help="Password to analyze"
    )

    hash_parser = subparsers.add_parser(
        "hash",
        help="Generate password hash"
    )

    hash_parser.add_argument(
        "--password",
        required=True,
        help="Password to hash"
    )

    hash_parser.add_argument(
        "--algorithm",
        required=True,
        choices=["md5", "sha1", "sha256", "sha512"],
        help="Hash algorithm"
    )

    identify_parser = subparsers.add_parser(
        "identify",
        help="Identify hash type"
    )

    identify_parser.add_argument(
        "--hash",
        required=True,
        help="Hash to identify"
    )

    crack_parser = subparsers.add_parser(
        "crack",
        help="Dictionary attack"
    )

    crack_parser.add_argument(
        "--hash",
        required=True,
        help="Target hash"
    )

    crack_parser.add_argument(
        "--algorithm",
        required=True,
        choices=["md5", "sha1", "sha256", "sha512"],
        help="Hash algorithm"
    )

    crack_parser.add_argument(
        "--wordlist",
        required=True,
        help="Path to wordlist"
    )

    args = parser.parse_args()

    match args.command:

        case "analyze":
            report = analyze_password(args.password)
            display_report(report)

        case "hash":
            result = hash_password(args.password, args.algorithm)
            console.print(f"[cyan]Hash:[/cyan] {result}")

        case "identify":
            result = identify_hash(args.hash)
            console.print(f"[cyan]Hash type:[/cyan] {result}")

        case "crack":
            result = crack_hash(args.hash, args.algorithm, args.wordlist)
            if result:
                console.print(f"[green]✓ Password found: {result}[/green]")
            else:
                console.print("[red]✗ Password not found[/red]")


if __name__ == "__main__":
    main()