# suplyd-odoo

## About

`suplyd-odoo` is a cli tool to run Suplyd's Odoo locally without any hasel.

## Requirements

1. `docker` should be installed on the system
2. Make sure python version is above `3.7`

## Installation

1. Install `sup-odoo` cli tool by running this command `pip install suplyd-odoo=1.2.9` ( https://pypi.org/project/suplyd-odoo/1.2.9/ )
2. Set alias for the command `python3 -m sup-odoo`/ `python -m sup-odoo` in your sell's `.rc` file
3. How to know which shell you are using `echo "$SHELL"`
   1. For example in a `zsh` shell you can update the `.zshrc` file by adding following line `alias sup-doo="python -m sup-odoo"` or `alias sup-doo="python3 -m sup-odoo"` at the top of it.
4. Once Odoo is running please ask Labeeb for a new DB backup zip file.

## Steps to run Odoo locally

### Start

1. To start the Odoo instance run this command `python3 -m sup-odoo start` or `python -m sup-odoo start`

### Stop

2. To stop the Odoo instance run this command `python3 -m sup-odoo stop` or `python -m sup-odoo stop`

### Clean

3. To stop the Odoo instance run this command `python3 -m sup-odoo clean` or `python -m sup-odoo clean`
