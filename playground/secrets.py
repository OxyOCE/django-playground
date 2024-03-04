from os import getenv

from dotenv import dotenv_values

def read_secrets():
    possible_secrets = ['DJANGO_SECRET_KEY']
    secrets = dotenv_values(".env")
    for key in possible_secrets:
        if key not in secrets:
            secrets[key] = getenv(key)

    return secrets
