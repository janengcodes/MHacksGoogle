"""questopia development configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'FIXME SET WITH: $ python3 -c "import os; print(os.urandom(24))" '
SESSION_COOKIE_NAME = 'login'
GOOGLE_API_KEY = 'AIzaSyCGu2PKA-ly-HGgkuiyswIPoVIUo64M9b4'

# File Upload to var/uploads/
QUESTOPIA_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = QUESTOPIA_ROOT/'var'/'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is var/insta485.sqlite3
# b'`\xa8\xb0B\x7fx\xc9(\xa9\xcc\xab1\xcbe\xc5-%\xb4\x82\xeaY\xca\xfbB'
