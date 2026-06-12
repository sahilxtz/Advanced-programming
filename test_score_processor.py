import os
import tempfile
import pytest
from score_processor import ScoreProcessor


class TestScoreProcessor:
    """Test suite for the ScoreProcessor class."""

    def setup_method(self):
        """Create a fresh ScoreProcessor instance before each test."""
        self.processor = ScoreProcessor()

    # ------------------------------------------------------------------ #
    # Happy-path tests                                                     #
    # ------------------------------------------------------------------ #

    def test_successful_calculation_with_valid_file(self, tmp_path):
        """A file containing '5' should return 50 (5 × 10)."""
        valid_file = tmp_path / "score.txt"
        valid_file.write_text("5")

        result = self.processor.process_score_file(str(valid_file))

        assert result == 50

    def test_calculation_with_large_score(self, tmp_path):
        """A file containing '100' should return 1000 (100 × 10)."""
        score_file = tmp_path / "score.txt"
        score_file.write_text("100")

        result = self.processor.process_score_file(str(score_file))

        assert result == 1000

    def test_calculation_with_zero(self, tmp_path):
        """A file containing '0' should return 0 (0 × 10)."""
        score_file = tmp_path / "score.txt"
        score_file.write_text("0")

        result = self.processor.process_score_file(str(score_file))

        assert result == 0

    def test_score_with_surrounding_whitespace(self, tmp_path):
        """Score surrounded by whitespace/newlines should still parse correctly."""
        score_file = tmp_path / "score.txt"
        score_file.write_text("  42\n")

        result = self.processor.process_score_file(str(score_file))

        assert result == 420

    # ------------------------------------------------------------------ #
    # Error-path tests                                                     #
    # ------------------------------------------------------------------ #

    def test_missing_file_raises_file_not_found_error(self):
        """Passing a non-existent path must raise FileNotFoundError."""
        with pytest.raises(FileNotFoundError):
            self.processor.process_score_file("/non/existent/path/score.txt")

    def test_invalid_content_raises_value_error(self, tmp_path):
        """A file containing letters instead of a number must raise ValueError."""
        bad_file = tmp_path / "bad_score.txt"
        bad_file.write_text("abc")

        with pytest.raises(ValueError):
            self.processor.process_score_file(str(bad_file))

    def test_empty_file_raises_value_error(self, tmp_path):
        """An empty file must raise ValueError (cannot parse empty string as int)."""
        empty_file = tmp_path / "empty.txt"
        empty_file.write_text("")

        with pytest.raises(ValueError):
            self.processor.process_score_file(str(empty_file))

    def test_float_string_raises_value_error(self, tmp_path):
        """A file containing a float like '3.14' must raise ValueError."""
        float_file = tmp_path / "float_score.txt"
        float_file.write_text("3.14")

        with pytest.raises(ValueError):
            self.processor.process_score_file(str(float_file))
