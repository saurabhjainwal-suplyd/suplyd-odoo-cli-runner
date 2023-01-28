# suplyd-odoo

## About

`suplyd-odoo` is a cli tool to run Suplyd's Odoo locally without any hasel.

## Requirements

1. `docker` should be installed on the system
2. Make sure python version is above `3.7`

## Installation

1. Install `sup-odoo` cli tool by running this command `pip install suplyd-odoo`

## Steps to run Odoo locally

1. To start the Odoo instance run this command `python3 -m sup-odoo start`/ `python -m sup-odoo start`
   1. Wait for the containers to start, keep in mind the first time could take a while to setup the containers
2. To stop the Odoo instance run this command `python3 -m sup-odoo stop`/ `python -m sup-odoo stop`
