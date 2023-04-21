
from pathlib import Path

ALLOWED_EXTENSIONS = tuple('csv')
UPLOAD_DIRECTORY = Path(__file__).parents[2] / 'uploads'


if not UPLOAD_DIRECTORY.exists():
    UPLOAD_DIRECTORY.mkdir() 