from .auth import auth
from .charts import charts
from .data import data
from .root import root
from .test import test
from .upload import upload

BLUEPRINTS = [auth, data, root, test, upload, charts]
