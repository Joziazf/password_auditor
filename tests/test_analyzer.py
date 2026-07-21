import pytest
from analyzer import analyze_password, PasswordReport


class TestCharacterClassDetection:

    def test_empty_password(self):
        report = analyze_password("")
        assert report.length == 0
        assert not report.has_uppercase
        assert not report.has_lowercase
        assert not report.has_digits
        assert not report.has_special
        assert report.score == 0
        assert report.strength == "weak"

    def test_only_lowercase(self):
        report = analyze_password("abcdefgh")
        assert report.has_lowercase
        assert not report.has_uppercase
        assert not report.has_digits
        assert not report.has_special

    def test_only_uppercase(self):
        report = analyze_password("ABCDEFGH")
        assert report.has_uppercase
        assert not report.has_lowercase

    def test_only_digits(self):
        report = analyze_password("12345678")
        assert report.has_digits
        assert not report.has_lowercase
        assert not report.has_uppercase

    def test_special_characters_detected(self):
        report = analyze_password("!@#$%^&*")
        assert report.has_special

    def test_unicode_letters_do_not_crash(self):
        report = analyze_password("пароль123")
        assert report.length == 9
        assert report.has_digits
        assert report.has_lowercase

    def test_whitespace_only_password(self):
        report = analyze_password("        ")
        assert report.length == 8
        assert not report.has_uppercase
        assert not report.has_lowercase
        assert not report.has_digits
        assert not report.has_special


class TestScoreBoundaries:

    @pytest.mark.parametrize(
        "password,expected_score",
        [
            ("a", 1),
            ("aaaaaaa", 1),
            ("aaaaaaaa", 2),
            ("abcdefg1", 3),
            ("Abcdefg123", 4),
            ("Abcdefg123!", 5),
            ("Abcdefghijk1!", 6),
        ],
    )
    def test_score_examples(self, password, expected_score):
        assert analyze_password(password).score == expected_score

    def test_length_8_boundary_adds_a_point(self):
        below = analyze_password("a" * 7)
        at_boundary = analyze_password("a" * 8)
        assert at_boundary.score == below.score + 1

    def test_length_12_boundary_adds_a_point(self):
        below = analyze_password("a" * 11)
        at_boundary = analyze_password("a" * 12)
        assert at_boundary.score == below.score + 1

    @pytest.mark.parametrize(
        "password,expected_strength",
        [
            ("abc", "weak"),     
            ("abcdefgh", "weak"),
            ("abcdefg1", "medium"),
            ("Abcdefg123", "medium"),
            ("Abcdefg123!", "strong"),
            ("Abcdefghijk1!", "strong"),
        ],
    )
    def test_strength_labels_at_boundaries(self, password, expected_strength):
        assert analyze_password(password).strength == expected_strength


class TestReturnType:
    def test_returns_password_report_instance(self):
        assert isinstance(analyze_password("x"), PasswordReport)