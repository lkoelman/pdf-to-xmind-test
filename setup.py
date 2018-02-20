#!/usr/bin/env python
'''
PdfToc2MindMap  setup

Warnings:
    to make pip respect the links, you have to use
    `--process-dependency-links` switch. So e.g.:
    `pip install --process-dependency-links <repo_path_or_url>`
'''

import setuptools

# see http://setuptools.readthedocs.io/en/latest/setuptools.html
# and https://packaging.python.org/tutorials/distributing-packages/
setuptools.setup(
    name='PdfToc2MindMap',
    version='0.1.0a1',
    install_requires=['pdfminer.six'],
    dependency_links=[
        'git+https://github.com/andrii-z4i/xmind-sdk-python.git@master-0'
    ],
    packages=setuptools.find_packages(exclude=('tests*',)), # find automatically
    author='Lucas Koelman',
    author_email='lucas.koelman@gmail.com',
    description='PdfToc2MindMap: create mindmaps from table of contents in a PDF file',
    long_description='PdfToc2MindMap: create mindmaps from table of contents in a PDF file',
    license='MIT',
    keywords=('pdf', 'mindmap', 'visualization'),
    url='https://github.com/mananatee/PdfToc2MindMap',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3',],
    entry_points={},
    package_data={})