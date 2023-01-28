#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

lib_name = "odoo"

setup(
    name="suplyd-odoo",
    version="1.2.4",
    description="Simple cli tool for Suplyd devs to run local Odoo setup without hassel",
    long_description="Simple cli tool for Suplyd devs to run local Odoo setup without hassel",
    url="https://github.com/saurabhjainwal-suplyd/suplyd-odoo-cli-runner",
    author="saurabhjainwal",
    author_email="saurabh@suplyd.app",
    license="MIT",
    scripts=[
        "./sup-odoo/__init__.py",
        "./sup-odoo/__main__.py",
        "./sup-odoo/docker-compose.yaml",
    ],
    packages=find_packages(),
    package_dir={"%s" % lib_name: "sup-odoo"},
    include_package_data=True,
    package_data={"": ["*.yaml"]},
    install_requires=["halo", "importlib_metadata", "setuptools", "twine"],
    python_requires=">=3.7",
)
