# notes techniques:

## lancer le serveur de test
```bash
python manage.py runserver
```

## initialisation de la bdd

source: https://docs.djangoproject.com/en/1.8/intro/tutorial01/

calcul du patch de migration de la bdd
```bash
python manage.py makemigrations ticket
```

Affichage du sql qui sera exécuté
```bash
python manage.py sqlmigrate ticket 0001
```

Exécution de la migration nécessaire
```bash
python manage.py migrate
```


## changement de BDD:
Faire les changements dans le paragraphe DATABASES de `octopus/settings.py`.
Lancer l'initialisation de la base:
```bash
python manage.py migrate
```
