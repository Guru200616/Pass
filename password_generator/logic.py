import random
import string


class PasswordConfigError(Exception):
    """Custom exception raised when password configuration is invalid."""
    pass


def build_character_pool(
    use_upper: bool,
    use_lower: bool,
    use_digits: bool,
    use_symbols: bool
) -> str:
    """
    Build a character pool string based on selected options.
    """
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise PasswordConfigError("No character sets selected.")

    return characters


def generate_password(
    length: int,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True
) -> str:
    """
    Generate a random password based on the given configuration.

    :param length: Length of the password (must be >= 4).
    :param use_upper: Include uppercase letters A-Z.
    :param use_lower: Include lowercase letters a-z.
    :param use_digits: Include digits 0-9.
    :param use_symbols: Include punctuation symbols.
    :return: Generated password string.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    characters = build_character_pool(
        use_upper=use_upper,
        use_lower=use_lower,
        use_digits=use_digits,
        use_symbols=use_symbols,
    )

    return "".join(random.choice(characters) for _ in range(length))
