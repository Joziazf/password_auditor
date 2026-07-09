import hashlib
import re

HASH_PATTERNS = {
        "MD5/NTLM": r"^[a-f0-9]{32}$",
        "SHA1":     r"^[a-f0-9]{40}$",
        "SHA256":   r"^[a-f0-9]{64}$",
        "SHA512":   r"^[a-f0-9]{128}$",
        "bcrypt":   r"^\$2[aby]\$\d{2}\$.{53}$",
    }

HASH_FUNCTIONS = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha256": hashlib.sha256,
        "sha512": hashlib.sha512,
    }

def identify_hash(hash_string: str) -> str:

    hash_string = hash_string.strip()
    for name, pattern in HASH_PATTERNS.items():
        if re.match(pattern, hash_string, re.IGNORECASE):
            return name
    return "Unknown"

def hash_password(password: str, algorithm: str) -> str:

    algorithm = algorithm.lower()

    if algorithm not in HASH_FUNCTIONS:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    return HASH_FUNCTIONS[algorithm](password.encode("utf-8")).hexdigest()