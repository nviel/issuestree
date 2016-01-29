# use of virtualenv with a debian based linux
install virtualenv with debian package because debian will not let you install it with pip (realy?)
```bash
sudo apt-get install python-virtualenv
```
create a new environment for your project:
```bash
virtualenv --no-site-packages /path/to/project/env_name_for_project
```
`--no-site-packages` option let you to safely separate system packages from your
environment packages.

activate your project environment:
```bash
source env_name_for_project/bin/activate
```

install django with pip:
```bash
pip install Django
```
I have experienced weird behaviour with pip behind a proxy...

# Use virtualenv with python3
FIXME!
