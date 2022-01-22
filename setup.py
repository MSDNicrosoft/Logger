# -*- coding: utf-8 -*- #
from setuptools import find_packages, setup

# Package Metadata
NAME = "msdnicrosoft_logger"
DESCRIPTION = "自己手写的 logger"
URL = "https://github.com/MSDNicrosoft/logger"
EMAIL = "wang3311835119@hotmail.com"
AUTHOR = "MSDNicrosoft"
REQUIRES_PYTHON = ">=3.6.0"
VERSION = "0.0.4"
REQUIRED = ["colorama>=0.4.4"]

try:
    with open("README.md", "r", encoding="utf-8") as desc:
        long_description = desc.read()
except FileNotFoundError:
    long_description = DESCRIPTION



setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=REQUIRED,
    include_package_data=True,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)
