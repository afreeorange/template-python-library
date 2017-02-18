"""
ACHTUNG: You *must* adapt the "install_requires", "setup_requires",
         and "tests_require" sections!
         Pin you dependencies!
         Classifiers are optional but recommended!
         I'll stop being excited now!
"""

import re

from setuptools import setup, find_packages

project_info = {}

with open('{}/__init__.py'.format('{{cookiecutter.package_name}}'), 'r') as f:
    for _ in f.read().splitlines():
        b = re.search(r'^__(.*)__\s*=\s*[\'"]([^\'"]*)[\'"]', _)
        if b:
            project_info[b.group(1)] = b.group(2)


setup(
    name=project_info['title'],
    version=project_info['version'],
    author=project_info['author'],
    author_email=project_info['author_email'],
    url=project_info['url'],
    license=project_info['license'],
    description=project_info['description'],
    long_description=open('README.md').read(),
    packages=[
        p for p
        in find_packages()
        if p not in ('tests', 'test')
    ],
    include_package_data=True,

    keywords='library component',
    install_requires=[
    ],
    setup_requires=[
        'pytest-runner',
        'wheel',

        {%- if cookiecutter.documentation_generator == 'reStructuredText' %}
        'Sphinx',
        'sphinx_rtd_theme',
        {%- elif cookiecutter.documentation_generator == 'Markdown' %}
        'mkdocs'
        {%- endif %}
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pytest-flake8',
        'pytest-watch',
    ],

    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3.6',
    ],
)
