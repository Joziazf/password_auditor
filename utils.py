from analyzer import PasswordReport

def display_report(report: PasswordReport) -> None:
    print("\nPassword Analysis")
    print("-" * 35)
    print(f"Length:        {report.length}")
    print(f"Uppercase:     {'✓' if report.has_uppercase else '✗'}")
    print(f"Lowercase:     {'✓' if report.has_lowercase else '✗'}")
    print(f"Digits:        {'✓' if report.has_digits else '✗'}")
    print(f"Special chars: {'✓' if report.has_special else '✗'}")
    print(f"Score:         {report.score}/6")
    print(f"Strength:      {report.strength}")