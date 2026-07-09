from analyzer import analyze_password, PasswordReport
from hash_utils import hash_password, identify_hash
from cracker import crack_hash

def display_menu() -> None:
    print("=" * 35)
    print("    Password Auditor")
    print("=" * 35)
    print("1. Analyze Password")
    print("2. Hash Utilities")
    print("3. Exit")


def display_report(report: PasswordReport) -> None:
    print("\nPassword Analysis")
    print("-" * 35)

    print(f"Length:        {report.length}")
    print(f"Uppercase:     {'✓' if report.has_uppercase else '✗'}")
    print(f"Lowercase:     {'✓' if report.has_lowercase else '✗'}")
    print(f"Digits:        {'✓' if report.has_digits else '✗'}")
    print(f"Special chars: {'✓' if report.has_special else '✗'}")
    print(f"Score:         {report.score}")
    print(f"Strength:      {report.strength}")


def run_password_analysis() -> None:
    password = input("Enter Password: ")
    report = analyze_password(password)
    display_report(report)
    input("Press Enter to continue...")

def run_hash_utilities() -> None:
    while True:
        print("\nHash Utilities")
        print("-" * 35)
        print("1. Generate Hash")
        print("2. Identify Hash")
        print("3. Crack Hash")
        print("4. Back")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                password = input("Enter password: ")
                algorithm = input("Algorithm (md5/sha1/sha256/sha512): ")

                try:
                    result = hash_password(password, algorithm)
                    print(f"\nHash: {result}")
                except ValueError as e:
                    print(f"Error: {e}")

            case "2":
                hash_string = input("Enter hash: ")
                result = identify_hash(hash_string)
                print(f"\nHash type: {result}")

            case "3":
                hash_string = input("Enter hash: ")
                algorithm = input("Algorithm (md5/sha1/sha256/sha512): ")
                wordlist_path = input("Wordlist path: ")

                try:
                    result = crack_hash(hash_string, algorithm, wordlist_path)
                    if result:
                        print(f"\n✓ Password found: {result}")
                    else:
                        print("\n✗ Password not found in wordlist")
                except FileNotFoundError as e:
                    print(f"Error: {e}")
                except ValueError as e:
                    print(f"Error: {e}")

            case "4":
                break

            case _:
                print("Invalid choice. Try again!")

def main() -> None:
    while True:
        print()

        display_menu()
        user_choice = input("Enter your choice: ")

        match user_choice:
            case "1":
                run_password_analysis()

            case "2":
                run_hash_utilities()

            case "3":
                print("Goodbye!")
                break

            case _:
                print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()