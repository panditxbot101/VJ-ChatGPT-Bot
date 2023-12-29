import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "26558147"))
API_HASH = environ.get("API_HASH", "ff188f7a9a2e29730d285afb200393dc")
BOT_TOKEN = environ.get("BOT_TOKEN", "6825090297:AAF28OlBRFouPfRbnMiPe0jdTOYPJMbx7G0")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002053554673"))
ADMINS = int(environ.get("ADMINS", "6229151120"))
DB_URI = environ.get("DB_URI", "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")
DB_NAME = environ.get("DB_NAME", "chatgptvjbot")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
