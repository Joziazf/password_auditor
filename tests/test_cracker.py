import pytest
from hash_utils import hash_password
from cracker import crack_hash


@pytest.fixture
def wordlist(tmp_path):
    content = "\n".join([
        "",
        "  password  ",
        "letmein",
        "",
        "dragon",
        "qwerty",
        "",
    ])
    path = tmp_path / "wordlist.txt"
    path.write_text(content, encoding="utf-8")
    return str(path)


class TestCrackHash:

    def test_finds_password_present_in_wordlist(self, wordlist):
        target = hash_password("dragon", "md5")
        result = crack_hash(target, "md5", wordlist)
        assert result == "dragon"

    def test_finds_password_that_needed_stripping(self, wordlist):
        target = hash_password("password", "md5")
        result = crack_hash(target, "md5", wordlist)
        assert result == "password"

    def test_returns_none_when_not_in_wordlist(self, wordlist):
        target = hash_password("not_in_the_list_xyz", "md5")
        result = crack_hash(target, "md5", wordlist)
        assert result is None

    def test_blank_lines_are_skipped_not_matched(self, wordlist):
        target = hash_password("", "md5")
        result = crack_hash(target, "md5", wordlist)
        assert result is None

    def test_missing_wordlist_raises_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            crack_hash("anyhash", "md5", "/path/does/not/exist.txt")

    def test_works_with_sha256_algorithm(self, wordlist):
        target = hash_password("qwerty", "sha256")
        result = crack_hash(target, "sha256", wordlist)
        assert result == "qwerty"

    def test_first_match_wins_on_duplicate_entries(self, tmp_path):
        path = tmp_path / "dupes.txt"
        path.write_text("dragon\ndragon\ndragon\n", encoding="utf-8")
        target = hash_password("dragon", "md5")
        result = crack_hash(target, "md5", str(path))
        assert result == "dragon"

    def test_wordlist_with_invalid_utf8_bytes_does_not_crash(self, tmp_path):
        path = tmp_path / "bad_encoding.txt"
        path.write_bytes(b"dragon\n\xff\xfe\nqwerty\n")
        target = hash_password("qwerty", "md5")
        result = crack_hash(target, "md5", str(path))
        assert result == "qwerty"