import os
from .base import *
from ..config.utils import *

JSON_PATH = os.path.join(Path(__file__).resolve().parent.parent, 'secret.json')
jsonData = read_json(JSON_PATH)

json = jsonData['production']
SECRET_KEY = json["SECRET_KEY"]


ALLOWED_HOSTS = [
    'localhost'
    ]


DATABASES ={
    "default": json["DATABASE"]["default"]
}

