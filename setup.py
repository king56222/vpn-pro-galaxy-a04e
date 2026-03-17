#!/usr/bin/env python3
# setup.py

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="vpn-pro-galaxy-a04e",
    version="3.0.0",
    author="king56222",
    author_email="Shahed20262026@hotmail.com",
    description="Professional VPN Application for Samsung Galaxy A04e",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/king56222/vpn-pro-galaxy-a04e",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Android",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Internet :: Proxy Servers",
        "Topic :: Security :: Cryptography",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "vpn-pro=src.main:main",
        ],
    },
)
