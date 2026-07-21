from dataclasses import dataclass
import string

SPECIALS = string.punctuation

@dataclass
class PasswordReport:
    length: int
    has_uppercase: bool
    has_lowercase: bool
    has_digits: bool
    has_special: bool
    score: int = 0
    strength: str = "Unknown"


def analyze_password(password: str) -> PasswordReport:
    report = PasswordReport(
        length=len(password),
        has_uppercase=any(c.isupper() for c in password),
        has_lowercase=any(c.islower() for c in password),
        has_digits=any(c.isdigit() for c in password),
        has_special=any(c in SPECIALS for c in password),
    )

    score = 0
    if report.length >= 8:
        score += 1
    if report.length >= 12:
        score += 1
    if report.has_uppercase:
        score += 1
    if report.has_lowercase:
        score += 1
    if report.has_digits:
        score += 1
    if report.has_special:
        score += 1

    report.score = score
    report.strength = (
        "weak" if score <= 2 else
        "medium" if score <= 4 else
        "strong"
    )

    return report