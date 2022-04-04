from setuptools import setup
from os import path
import io

this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="python-flexpolyline-pbapi",
    description="Flexible Polyline encoding (PBAPI extension)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.1.0",
    author="decitre",
    packages=["flexpolyline_pbapi"],
    # SPDX-License-Identifier: MIT
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Source": "https://github.com/decitre/python-flexpolyline-pbapi.git"
    },
    test_suite="test_flexpolyline"
)
