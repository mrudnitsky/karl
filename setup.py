from setuptools import setup, find_packages
import os
find_packages()

def read_file(fname):
    """
    return file contents
    :param fname: path relative to setup.py
    :return: file contents
    """
    with open(os.path.join(os.path.dirname(__file__), fname), "r") as fd:
        return fd.read()


setup(
    name="karl",
    version="0.2.5",
    license="MIT",
    author="Daniel Luca",
    author_email="daniel.luca@consensys.net",
    long_description=read_file("Readme.md") if os.path.isfile("Readme.md") else "",
    packages=["karl"],
    requires=["mythril", "web3"],
    long_description_content_type="text/markdown",
    entry_points={"console_scripts": ["karl=karl.interfaces.cli:main"]},
    credits="Bernhard Mueller",
)
