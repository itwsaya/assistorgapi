#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = []

test_requirements = []

setup(
    name='assistorg-api',
    version='0.0.2',
    description="Unofficial API wrapper for ASSIST.org's API.",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    author="Glenn Benedict Montesclaros",
    author_email='montesclarosglennbenedict@gmail.com',
    url='https://github.com/montesclarosglennbenedict/assist_api_wrapper',
    packages=find_packages(include=['assist_api_wrapper', 'assist_api_wrapper.*']),
    python_requires='>=3.6',
    install_requires=requirements,
    tests_require=test_requirements,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    license="MIT license",
    zip_safe=False,
)
