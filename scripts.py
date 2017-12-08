#!venv/bin/python
from flask_script import Manager
import os


manager = Manager(app)


@manager.command
def sample_script():
    print("Sample script initiated")