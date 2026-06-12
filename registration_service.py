"""
RegistrationService — core validation module for user onboarding.

Business rules enforced:
  1. Email must not be None or empty.
  2. Email must match the standard format: identifier@domain.tld
     Regex: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
  3. Applicant must be at least 18 years old.
"""

import re
from exceptions import InvalidEmailError, UnderageError

# Standard email regex (as discussed in slides)
_EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9._%+\-]+"   # local part (identifier)
    r"@"                       # @ symbol (mandatory separator)
    r"[a-zA-Z0-9.\-]+"        # domain name
    r"\.[a-zA-Z]{2,}$"        # top-level domain (min 2 chars)
)

MINIMUM_AGE = 18


class RegistrationService:
    """Validates and processes new user registration requests."""

    def __init__(self, enabled: bool = True):
        """
        :param enabled: Flag that represents whether the registration
                        system is active. Used by the internal assert.
        """
        self.enabled = enabled

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def register_user(self, email: str, age: int) -> bool:
        """
        Validate *email* and *age*, then approve or deny registration.

        :param email: Applicant's e-mail address.
        :param age:   Applicant's age in years.
        :returns:     True when the registration succeeds.
        :raises InvalidEmailError: If the email is absent or malformed.
        :raises UnderageError:     If the applicant is under 18.
        """
        # ── Internal invariant ────────────────────────────────────────
        # The service must be enabled before processing any registration.
        # This guards against misconfigured or disabled contexts.
        assert self.enabled, (
            "RegistrationService is currently disabled; "
            "cannot process registrations."
        )

        # ── Rule 1 & 2: Email validation ──────────────────────────────
        self._validate_email(email)

        # ── Rule 3: Age validation ────────────────────────────────────
        self._validate_age(age)

        # All checks passed → registration approved
        return True

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _validate_email(self, email: str) -> None:
        """Raise InvalidEmailError if *email* is absent or malformed."""
        if not email:                          # catches None and ""
            raise InvalidEmailError(email)
        if not _EMAIL_REGEX.match(email):
            raise InvalidEmailError(email)

    def _validate_age(self, age: int) -> None:
        """Raise UnderageError if *age* is below the minimum threshold."""
        if age < MINIMUM_AGE:
            raise UnderageError(age)
