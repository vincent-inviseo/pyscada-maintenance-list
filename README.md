# PyScada Maintenance Plugin

This PyScada plugin allow PyScada application to register some devices need periodic maintenance

## How that works

This plugin allows pyscada user to register device (may be different device on pyscada administration) which need perodic maintenance and then follow them

## Installation

First, download this projet using git
```
# Download plugin
git clone git@github.com:vincent-inviseo/pyscada-maintenance-list.git
# Activate virutal env PyScada
source /home/pyscada/.venv/bin/activate
# Install plugin
sudo -u pyscada -E env PATH=${PATH} pip3 install -e ./pyscada-maintenance-list
```

After restart gunicorn
```
systemctl restart guncorn
```

## How to use

- TODO


## Lisence

The project is licensed under the _GNU AFFERO GENERAL PUBLIC LICENSE Version 3 (AGPLv3)_.
