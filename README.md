# recipe-app-api

## config
```bash
# create docker-compose.yml and run build
docker-compose build

# create django project inside docker
docker-compose run app sh -c "django-admin.py startproject app ." 

# run app by dockercompose
docker-compose run app sh -c "python manage.py test && flake8"

# create django app core
sudo docker-compose run app sh -c "python manage.py startapp core"
```

## TDD test drive development
sederhananya adalah melakukan tetsing sebelum menulis code