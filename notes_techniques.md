# notes techniques:

source: https://docs.djangoproject.com/en/1.8/intro/tutorial01/

```bash
python manage.py makemigrations ticket
```
calcul le patch de migration de la bdd

```bash
python manage.py sqlmigrate ticket 0001
```
retourne le sql qui sera exécuté

```bash
python manage.py migrate
```
exécute la migration nécessaire
