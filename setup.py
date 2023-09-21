import os

from setuptools import find_packages, setup

executables = [
    f for f in os.listdir(".") if os.path.isfile(f) and os.access(f, os.X_OK)
]

setup(
    name="quiver",
    version="0.1",
    packages=find_packages(),
    scripts=executables,
)
