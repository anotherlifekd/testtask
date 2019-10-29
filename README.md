# Installation

## Copy project


```bash
git copy https://github.com/anotherlifekd/testtask.git
```

## Usage

```bash
docker build .
docker-compose run --rm web python /code/src/manage.py migrate --noinput
docker-compose run --rm web python /code/src/manage.py create_states
docker-compose run --rm web python /code/src/manage.py create_clients
docker-compose run --rm web python /code/src/manage.py createsuperuser
docker-compose up --build
```
