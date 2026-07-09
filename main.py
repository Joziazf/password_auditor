from analyzer import analyze_password, PasswordReport


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

def main() -> None:
    while True:
        print()

        display_menu()
        user_choice = input("Enter your choice: ")

        match user_choice:
            case "1":
                run_password_analysis()

            case "2":
                print("Hash Utilities - Coming Soon")

            case "3":
                print("Goodbye!")
                break

            case _:
                print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()