# 2023_wa_sa_hutnikova_gaflix

## Pri inicilaizaci projktu

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

## Spusteni projektu

```
git pull
source ./venv/Scripts/activate
./manage.py migrate
./manage.py runserver
```

## Po zmene `models.py`

```
./manage.py makemigrations
./manage.py migrate
```

## Reset databaze

```
rm db.sqlite3
./manage.py migrate
./manage.py loaddata fixtures/*.json
```