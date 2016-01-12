## What is it?

This is a prototype for a "yet another bugtracker!"

**This prototype is under development and is not functional yet.**

The aim is to test some features that  are rarely implemented anywhere else. For example:
* Use of a tree structure and an efficient tree view.
* Use of absolute sort.
* ...


## Install
```bash
sudo apt-get install python-django
```
Yes it use django... Why not? This is a prototype.

**FIXME**: do not forget the database manager!


```bash
git clone https://github.com/nviel/issuestree
```

database initialization:
configure the DATABASES dict in `octopus/settings.py`


## Who to launch development server
```bash
cd issuestree
python manage.py runserver [port (default is 8000)]
```

Then visit the site at `http://localhost:8000`

## Technical notes:
* python 2.7 (but I will switch to 3.x soon)
* django 
* jquery
* jstree
* mysql or postgreSQL


## Update from an older version
Eh! This is a prototype you should not have an older version! Or it must not be in production and no migration is necessary.
I will see this point later.
