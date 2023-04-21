from .auth import auth
from .data import data
from .root import root
from .test import test
from .upload import upload

BLUEPRINTS = [
    auth,
    data,
    root,
    test,
    upload
]