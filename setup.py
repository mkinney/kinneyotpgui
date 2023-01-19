# Note: you shouldn't need to run this script manually.
# It is run implicitly by the pip3 install command.
"""Setup script for kinneyotpgui"""

import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# This call to setup() does all the work
setup(
    name="kinneyotpgui",
    version="0.0.6",
    description="Graphical user interface for one time pad",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mike Kinney",
    author_email="mike.kinney@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.10",
    ],
    packages=["kinneyotpgui"],
    include_package_data=True,
    package_data={},
    install_requires=["pyside6", "kinneyotp"],
    extras_require={},
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "otp=kinneyotpgui.main:main",
        ]
    },
)
