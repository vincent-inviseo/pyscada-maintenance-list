# PyScada Maintenance Plugin

This PyScada plugin allow PyScada application to register some devices need periodic maintenance

## How that works

This plugin allows pyscada user to register device (may be different device on pyscada administration) which need perodic maintenance and then follow them.

It's automatically create a widget model `MaintenanceWidgetContent[1] Liste de maintenance` listed on content widget list. This list of maintenance it's unique and can be have 0 or more device needed maintenance.

Then, you will found in PyScada administration a section `PYSCADA MAINTENANCELIST` with 3 sub sections :

### Maintenance device type

That's the place you will register types of device (security, confort, electric) which can you to group device by function

To add a type you must fill form with unique and required property `Type of device`

This property will have interest for futurs developpment when we integrate `filters` and `sorting`

### Maintenance devices

That's the place you will register devices (fire detector, elevator, extinguisher, mechanical ventilation ... )

To add a device fill form with properties :

- `Reference`: (optional) Indicate here a device's reference like own internal code (ref_001), serial number or other. This field it's an arbitrary value
- `Locate`: (optional) Indicate here where is the device (for example `technical room floor 1`)
- `Name`: (required) Indicate  freindly name for common usages (securitydoor_west01)
- `Type`: (optional) Select a type previously registred
- `Created at`: (required) Indicate here when you have registered device. By default it's current date and time but you can select later or older
- `Updated at`: (optional) Indaicate here last time device was updated. By default it's current date and time but you can select as you want
- `Select maintenance period`: Select a maintenance frequency (each month, each 3 months, each 4 months, each year, each 2 years)
- `description`: (optional) You can put here anythings about the device. For example you can write all maintenances will do or technical description

### Maintenance

That's the place where you will register a maintenance on a device. Device can has 0 or many maintenances. With this list we have historical maintenance about each devices

To add a maintenance fill form with properties :
- `Make at`: (required) Indicate here date and time when the maintenance has been done
- `Device is conform after control`: (optional) It's a boolean to indication if this device fills conditions to be conform to the maintenance. If case is check this device is declare as `conform`. Otherwhise device is declare as `no conform`
- `Maintener`: (optional) List all PyScada Users to selection. This value indicate who did maintenance (or validate it)
- `Report url join`: (optional) `Maintener` can left an url to local storage or web maintenance report
- `Maintenance Device`: (required) select device related at this maitenance

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

You need have `page`.
Create new widget with `Content` value `MaintenanceWidgetContent[1] Liste de maintenance`.

Your list will be initially empty and you must will fill with `Maintenance devices` and `Maintenances`.

## Lisence

The project is licensed under the _GNU AFFERO GENERAL PUBLIC LICENSE Version 3 (AGPLv3)_.
