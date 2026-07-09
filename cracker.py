from hash_utils import hash_password
from pathlib import Path

def crack_hash(target_hash: str, algorithm: str, wordlist_path: str) -> str | None:
    wordlist = Path(wordlist_path)

    if not wordlist.exists():
        raise FileNotFoundError(f"Wordlist not found: {wordlist_path}")

    with wordlist.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            password = line.strip()

            if not password:
                continue

            if hash_password(password, algorithm) == target_hash:
                return password

    return None