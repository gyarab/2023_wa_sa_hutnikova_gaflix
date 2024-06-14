# 2024_wa_sa_hutnikova_gaflix

## První inicializace projektu

```
git clone git@github.com:gyarab/2023_wa_sa_hutnikova_gaflix.git
cd 2023_wa_sa_hutnikova_gaflix/

py -3 -m venv venv
source ./venv/Scripts/activate

pip install -r requirements.txt

./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

## Spuštění projektu

```
git pull
source ./venv/Scripts/activate
./manage.py migrate
./manage.py runserver
```

## Po změně `models.py`

```
./manage.py makemigrations
./manage.py migrate
```

## Reset databáze

```
rm db.sqlite3

./manage.py migrate

./manage.py loaddata fixtures/*.json
```