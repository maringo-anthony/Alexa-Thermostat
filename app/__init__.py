from flask import Flask

app = Flask(__name__)
from app import routes  # may cause issues that this is up here
