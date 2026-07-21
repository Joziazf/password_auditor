# Password Auditor

CLI security tool for password analysis and hash cracking.

> ⚠️ **For educational and authorized security testing purposes only.** 
> Only use against hashes/systems you own or have explicit permission to test.

## Features

- **Password strength analysis** — checks length, character variety, scores 0–6
- **Hash generation** — MD5, SHA1, SHA256, SHA512
- **Hash identification** — pattern-based detection (regex on length/format)
- **Dictionary attack** — brute-force a hash against a wordlist

## Installation

- git clone https://github.com/Joziazf/password_auditor
- cd password_auditor
- pip install -r requirements.txt

## Usage

### Analyze password strength
python main.py analyze --password 'MyPassword123!'

### Generate hash
python main.py hash --password 'dragon' --algorithm md5

### Identify hash type
python main.py identify --hash '8621ff...'

### Dictionary attack
python main.py crack --hash '8621ff...' --algorithm md5 --wordlist wordlists/test.txt

### Tests:
pytest tests/ -v

## Supported algorithms
- MD5, SHA1, SHA256, SHA512

## Known limitations

- Hash identification is pattern-based (length/format), not cryptographically certain — MD5 and NTLM are indistinguishable this way.
- Dictionary attack currently supports **unsalted** hashes only. Salted hashes (`salt:hash` format, PBKDF2, bcrypt) are not yet supported.
- No rainbow table or rule-based mutation support — pure dictionary lookup.