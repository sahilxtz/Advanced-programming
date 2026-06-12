"""
Test suite for RegistrationService.

Run with:  pytest test_registration_service.py -v
"""

import pytest
from registration_service import RegistrationService
from exceptions import InvalidEmailError, UnderageError


# ══════════════════════════════════════════════════════════════════════
# Fixture  (shared setup — analogous to @BeforeEach in JUnit)
# ══════════════════════════════════════════════════════════════════════

@pytest.fixture
def service():
    """Provide a fresh, enabled RegistrationService for each test."""
    return RegistrationService(enabled=True)


@pytest.fixture
def disabled_service():
    """Provide a disabled RegistrationService for invariant tests."""
    return RegistrationService(enabled=False)


# ══════════════════════════════════════════════════════════════════════
# Happy-path tests
# ══════════════════════════════════════════════════════════════════════

class TestSuccessfulRegistration:

    def test_valid_email_and_adult_age_returns_true(self, service):
        assert service.register_user("alice@example.com", 25) is True

    def test_minimum_age_boundary_is_accepted(self, service):
        """Exactly 18 must be allowed (boundary value analysis)."""
        assert service.register_user("bob@domain.org", 18) is True

    def test_email_with_plus_tag_is_valid(self, service):
        assert service.register_user("user+tag@mail.co", 30) is True

    def test_email_with_subdomain_is_valid(self, service):
        assert service.register_user("name@sub.domain.com", 22) is True

    def test_email_with_dots_in_local_part(self, service):
        assert service.register_user("first.last@company.io", 40) is True


# ══════════════════════════════════════════════════════════════════════
# InvalidEmailError tests
# ══════════════════════════════════════════════════════════════════════

class TestInvalidEmailError:

    def test_empty_string_raises_invalid_email(self, service):
        with pytest.raises(InvalidEmailError):
            service.register_user("", 25)

    def test_none_email_raises_invalid_email(self, service):
        with pytest.raises(InvalidEmailError):
            service.register_user(None, 25)

    def test_missing_at_symbol_raises_invalid_email(self, service):
        with pytest.raises(InvalidEmailError):
            service.register_user("invalidemail.com", 25)

    def test_missing_domain_raises_invalid_email(self, service):
        with pytest.raises(InvalidEmailError):
            service.register_user("user@", 25)

    def test_missing_tld_raises_invalid_email(self, service):
        with pytest.raises(InvalidEmailError):
            service.register_user("user@domain", 25)

    def test_double_at_symbol_raises_invalid_email(self, service):
        with pytest.raises(InvalidEmailError):
            service.register_user("user@@domain.com", 25)

    def test_spaces_in_email_raises_invalid_email(self, service):
        with pytest.raises(InvalidEmailError):
            service.register_user("user @domain.com", 25)

    def test_error_message_contains_bad_email(self, service):
        bad_email = "not-an-email"
        with pytest.raises(InvalidEmailError) as exc_info:
            service.register_user(bad_email, 25)
        assert bad_email in str(exc_info.value)

    def test_error_message_for_empty_email(self, service):
        with pytest.raises(InvalidEmailError) as exc_info:
            service.register_user("", 25)
        assert "null or empty" in str(exc_info.value).lower() or \
               "not be" in str(exc_info.value).lower()


# ══════════════════════════════════════════════════════════════════════
# UnderageError tests
# ══════════════════════════════════════════════════════════════════════

class TestUnderageError:

    def test_age_17_raises_underage_error(self, service):
        with pytest.raises(UnderageError):
            service.register_user("valid@example.com", 17)

    def test_age_zero_raises_underage_error(self, service):
        with pytest.raises(UnderageError):
            service.register_user("valid@example.com", 0)

    def test_negative_age_raises_underage_error(self, service):
        with pytest.raises(UnderageError):
            service.register_user("valid@example.com", -5)

    def test_age_boundary_one_below_minimum_raises(self, service):
        """17 is the boundary just below the minimum — must be rejected."""
        with pytest.raises(UnderageError):
            service.register_user("valid@example.com", 17)

    def test_error_message_contains_supplied_age(self, service):
        with pytest.raises(UnderageError) as exc_info:
            service.register_user("valid@example.com", 15)
        assert "15" in str(exc_info.value)

    def test_underage_error_inherits_from_value_error(self, service):
        with pytest.raises(ValueError):
            service.register_user("valid@example.com", 16)


# ══════════════════════════════════════════════════════════════════════
# Exception hierarchy / inheritance tests
# ══════════════════════════════════════════════════════════════════════

class TestExceptionHierarchy:

    def test_invalid_email_error_is_value_error(self, service):
        with pytest.raises(ValueError):
            service.register_user("bad-email", 25)

    def test_underage_error_is_value_error(self, service):
        with pytest.raises(ValueError):
            service.register_user("good@email.com", 10)


# ══════════════════════════════════════════════════════════════════════
# Internal assert / invariant test
# ══════════════════════════════════════════════════════════════════════

class TestInvariantAssertion:

    def test_disabled_service_raises_assertion_error(self, disabled_service):
        """When the service is disabled the assert must fire."""
        with pytest.raises(AssertionError):
            disabled_service.register_user("valid@example.com", 25)
