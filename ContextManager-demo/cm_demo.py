#!/usr/bin/python3 #-i
from contextlib import contextmanager
import os

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with change_dir('../Factorisation-P3'):
    print(os.listdir())

with change_dir('../SQLite-demo'):
    print(os.listdir())