from setuptools import setup
from setuptools.command.sdist import sdist as _sdist
import shutil
from os import path
import io

this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


class sdist(_sdist):
    def run(self):
        shutil.copy('LICENSE', 'LICENSE')
        _sdist.run(self)

setup(
    name='python-flexpolyline-pbapi',
    description='Flexible Polyline encoding (PBAPI extension)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.1.0',
    author='HERE Europe B.V.',
    url='https://here.com',
    packages=['flexpolyline_pbapi'],
    # SPDX-License-Identifier: MIT
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License'
    ],
    project_urls={
        'Source': 'https://github.com/heremaps/flexible-polyline.git'
    },
    test_suite="test_flexpolyline",
    cmdclass={'sdist': sdist}
)
