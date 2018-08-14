"""setup.py"""
from setuptools import setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    author="Beau Barker",
    description="Apply values to optional params",
    long_description=readme,
    long_description_content_type="text/markdown",
    name="apply_defaults",
    packages=["apply_defaults"],
    url="https://github.com/bcb/apply_defaults",
    version="0.1.0",
)
