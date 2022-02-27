import os

# Config helpers


class ConfigError(KeyError):
    def __init__(self, key: str, *args: object) -> None:
        super().__init__(f"Environment variable '{key}' required but not defined!", *args)


def env(key: str, default: str = None, required: bool = True):
    value = os.environ.get(key, default)

    if required and value is None:
        raise ConfigError(key)
    else:
        return value


# Config classes


db = dict(
    url=env("DB_URL")
)
