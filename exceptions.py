"""
Custom exceptions for the user onboarding validation module.

InvalidEmailError  → inherits from ValueError  (bad input value)
UnderageError      → inherits from ValueError  (bad input value)
"""


class InvalidEmailError(ValueError):
    """Raised when the supplied e-mail address is None, empty, or
    does not conform to the standard email format."""

    def __init__(self, email: str):
        self.email = email
        if email is None or email == "":
            message = "Email address must not be null or empty."
        else:
            message = (
                f"'{email}' is not a valid email address. "
                "Expected format: identifier@domain.tld"
            )
        super().__init__(message)


class UnderageError(ValueError):
    """Raised when an applicant is younger than the minimum required age (18)."""

    MINIMUM_AGE = 18

    def __init__(self, age: int):
        self.age = age
        message = (
            f"Applicant age {age} does not meet the minimum age requirement "
            f"of {self.MINIMUM_AGE}. Registration denied."
        )
        super().__init__(message)
