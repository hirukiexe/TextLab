import random
import string
from faker import Faker

fake = Faker()

# Allowed characters for username
LETTERS_DIGITS = string.ascii_lowercase + string.digits
SPECIAL_CHARS = "-_."  # special characters allowed inside

def generate_random_username(length=8):
    """
    Generate a valid username for email:
    - Starts and ends with letter/digit
    - No consecutive special characters
    """
    if length < 3:
        length = 3  # minimum length

    username = random.choice(LETTERS_DIGITS)  # first character (cannot be special)

    while len(username) < length - 1:
        prev = username[-1]
        # Decide next character
        if prev in SPECIAL_CHARS:
            # After special char, must be letter/digit
            next_char = random.choice(LETTERS_DIGITS)
        else:
            # Can be letter/digit or special
            next_char = random.choice(LETTERS_DIGITS + SPECIAL_CHARS)
        username += next_char

    # Last character must be letter/digit
    username += random.choice(LETTERS_DIGITS)
    return username

def generate_name_username(length=6):
    """
    Generate username based on random name + number:
    - No consecutive special characters
    - Safe for email
    """
    while True:
        name = fake.first_name().lower()
        number = ''.join(random.choices(string.digits, k=length))
        username = f"{name}{number}"[:20]  # max 20 chars

        # Check for invalid start/end or consecutive specials
        if username[0] in SPECIAL_CHARS or username[-1] in SPECIAL_CHARS:
            continue
        invalid = any(username[i] in SPECIAL_CHARS and username[i+1] in SPECIAL_CHARS
                      for i in range(len(username)-1))
        if invalid:
            continue
        return username

# Domain mapping
domain_map = {
    "gmail": "@gmail.com",
    "hotmail": "@hotmail.com",
    "yahoo": "@yahoo.com",
    "outlook": "@outlook.com",
    "icloud": "@icloud.com",
    "zoho": "@zoho.com",
    "gmx": "@gmx.com",
    "mailru": "@mail.ru",
    "yandex": "@yandex.com",
    "protonmail": "@protonmail.com"
}

def generate_mail(domain_type="all", mail_type="unique", count=10):
    emails = []

    # Prepare domains
    if domain_type == "all":
        domains = list(domain_map.values())
    else:
        domain = domain_map.get(domain_type.lower())
        if not domain:
            raise ValueError(f"Unknown domain_type: {domain_type}")
        domains = [domain]

    while len(emails) < count:
        domain = random.choice(domains)

        if mail_type.lower() == "name":
            username = generate_name_username(length=4)
        else:
            username = generate_random_username(length=8)

        email = f"{username}{domain}"
        if email not in emails:
            emails.append(email)

    return emails