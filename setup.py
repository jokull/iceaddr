# -*- encoding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iceaddr",
    version="0.1.0",
    author="Sveinbjorn Thordarson",
    author_email="sveinbjorn@sveinbjorn.org",
    license='BSD',
    url="https://github.com/sveinbjornt/iceaddr",
    description="Look up information about Icelandic street addresses and postcodes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'sqlite3',
        'pkg_resources'
    ],
    packages=['iceaddr'],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: Icelandic",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Topic :: Text Processing :: Linguistic"
    ],
    include_package_data=True,
    zip_safe=False
)
