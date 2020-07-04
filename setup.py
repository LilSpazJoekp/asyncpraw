"""asyncpraw setup.py"""

import re
from codecs import open
from os import path

from setuptools import find_packages, setup

PACKAGE_NAME = "asyncpraw"
HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, "README.rst"), encoding="utf-8") as fp:
    README = fp.read()
with open(path.join(HERE, PACKAGE_NAME, "const.py"), encoding="utf-8") as fp:
    VERSION = re.search('__version__ = "([^"]+)"', fp.read()).group(1)

extras = {
    "ci": ["coveralls"],
    "dev": ["pre-commit"],
    "lint": [
        "black",
        "flake8",
        "pydocstyle",
        "sphinx<3.0",
        "sphinx_rtd_theme",
        "sphinxcontrib-trio",
    ],
    "test": [
        "pytest >=2.7.3",
        "asynctest >=0.13.0",
        "vcrpy @ git+https://github.com/LilSpazJoekp/vcrpy.git#egg=vcrpy-4.0.2",  # temporary fix
        "pytest-vcr",
        "mock >=0.8",
        "testfixtures >4.13.2, <7",
    ],
}
extras["dev"] += extras["lint"] + extras["test"]

setup(
    name=PACKAGE_NAME,
    author="Joel Payne",
    author_email="lilspazjoekp@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
    ],
    description=(
        "PRAW, an acronym for `Python Reddit API Wrapper`, is a "
        "python package that allows for simple access to "
        "reddit's API."
    ),
    extras_require=extras,
    install_requires=[
        "asyncprawcore >=1.0.1, <2.0",
        "update_checker >=0.17",
        "websockets >=8.1",
    ],
    keywords="reddit api wrapper async",
    license="Simplified BSD License",
    long_description=README,
    package_data={"": ["LICENSE.txt"], PACKAGE_NAME: ["*.ini", "images/*.jpg"]},
    packages=find_packages(exclude=["tests", "tests.*", "tools", "tools.*"]),
    url="https://asyncpraw.readthedocs.org/",
    version=VERSION,
)
