import hashlib
import pytest
from hash_utils import identify_hash, hash_password


class TestIdentifyHash:

    def test_md5_length_32_identified_as_md5_ntlm(self):
        md5_of_dragon = hashlib.md5(b"dragon").hexdigest()
        assert identify_hash(md5_of_dragon) == "MD5/NTLM"

    def test_sha1_length_40(self):
        sha1_of_dragon = hashlib.sha1(b"dragon").hexdigest()
        assert identify_hash(sha1_of_dragon) == "SHA1"

    def test_sha256_length_64(self):
        sha256_of_dragon = hashlib.sha256(b"dragon").hexdigest()
        assert identify_hash(sha256_of_dragon) == "SHA256"

    def test_sha512_length_128(self):
        sha512_of_dragon = hashlib.sha512(b"dragon").hexdigest()
        assert identify_hash(sha512_of_dragon) == "SHA512"

    def test_bcrypt_format(self):
        fake_bcrypt = "$2b$12$" + "a" * 53
        assert identify_hash(fake_bcrypt) == "bcrypt"

    def test_unknown_format_returns_unknown(self):
        assert identify_hash("not_a_hash_at_all") == "Unknown"

    def test_empty_string_returns_unknown(self):
        assert identify_hash("") == "Unknown"

    def test_uppercase_hex_is_still_identified(self):
        md5_upper = hashlib.md5(b"dragon").hexdigest().upper()
        assert identify_hash(md5_upper) == "MD5/NTLM"

    def test_surrounding_whitespace_is_stripped(self):
        sha1_of_dragon = hashlib.sha1(b"dragon").hexdigest()
        assert identify_hash(f"  {sha1_of_dragon}  ") == "SHA1"

    def test_wrong_length_hex_is_unknown(self):
        almost_md5 = "a" * 31
        assert identify_hash(almost_md5) == "Unknown"

    def test_non_hex_characters_rejected(self):
        bad_chars = "g" * 32
        assert identify_hash(bad_chars) == "Unknown"


class TestHashPassword:

    def test_md5_matches_hashlib(self):
        assert hash_password("dragon", "md5") == hashlib.md5(b"dragon").hexdigest()

    def test_sha1_matches_hashlib(self):
        assert hash_password("dragon", "sha1") == hashlib.sha1(b"dragon").hexdigest()

    def test_sha256_matches_hashlib(self):
        assert hash_password("dragon", "sha256") == hashlib.sha256(b"dragon").hexdigest()

    def test_sha512_matches_hashlib(self):
        assert hash_password("dragon", "sha512") == hashlib.sha512(b"dragon").hexdigest()

    def test_algorithm_is_case_insensitive(self):
        assert hash_password("dragon", "MD5") == hash_password("dragon", "md5")

    def test_unsupported_algorithm_raises_value_error(self):
        with pytest.raises(ValueError):
            hash_password("dragon", "bcrypt")

    def test_empty_password_hashes_without_error(self):
        assert hash_password("", "md5") == hashlib.md5(b"").hexdigest()

    def test_unicode_password_hashes_via_utf8(self):
        password = "пароль"
        assert hash_password(password, "sha256") == hashlib.sha256(
            password.encode("utf-8")).hexdigest()