# Password Auditor

CLI security tool for password analysis and hash cracking.

## Installation

- git clone https://github.com/Joziazf/password_auditor
- cd password-auditor
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

## Supported algorithms
- MD5, SHA1, SHA256, SHA512