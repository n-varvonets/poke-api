# GitHub Actions status:
 - Status of last Deployment: <br>
<img src="https://github.com/n-varvonets/poke-api/workflows/CI-CD-PokeApi-to-AWS-ElasticBeanstalk/badge.svg?branch=main"><br>

# Stack of tech:
- Python 3.10.9
- Django 4.1.6
- GitHub Actions
- RDS
- Elastic Beanstalk
- Rout53, SSL

# Task:
Создать ВЕБ Сервис - “Pokeapi”:
Дать возможность зарегистрироваться игроку.
Игроки могут выбирать себе покемонов(list,get - look viewsets) для игры в личном кабинете.

Также сделать список всех игроков и их покемонов с возможностью  извлечения по API.

Технические требования
Stack технологий:
Django(DRF)/ Flask/ FastAPI
PostgreSQL
Docker, Docker-Compose
pytest/unitest

PokéAPI Этот веб-сайт предоставляет интерфейс RESTful API для высокодетализированных объектов, построенных из тысяч
строк данных, связанных с покемонами. Использовать этот ресурс для сбора данных. Предоставить возможность перехода  на новый ресурс предоставления данных.
Покрыть тестами регистрацию и выбор покемонов. При тестированиИ и все запросы на сторонние ресурсы замокать.
Результат работы должен быть представлен на GitHub. Для запуска должно быть достаточно выполнить:
git clone
docker-compose up --build

#  Elastic Beanstalk
It's service for deploying and scaling web applications and services developed
    - with lang:Java, dotnet, PHP, NodeJS, Python, Ruby, Go 
    - and docker familiar services: Apache, NGINX, passenger, and IIS.

You can simply upload your code and elastic Beanstalk automatically handles the deployment from:
    - capacity provisioning(забезпечення потужності),
    - load balancing,
    - auto-scaling applications,
    - health monitoring.

The same time you will_retain_full(сохранит полную) control over database
resources powering your application can access than their land resources at anytime

Elastic Beanstalk is THE FASTEST AND SIMPLEST way to deploy your application on AWS

Core concepts(similar to folder):
    - Application: our logic of web-app
    - Application Version: labeled iteration of deployed code
    - Environment: collection of DB-resources running on an application version

We can use it by:
       - cli
       - AWS web-app

% mariadb-devel - иногда mysql может давать ошибку, поєтому используем "мариюдб"
1)
eb init -p python-3.8 poke-eb-project
(aws-access-id): AKIASBKR2UWDPVFNX3PL
(aws-secret-key): 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
eb init -p python-3.8 poke-eb-project --region 'eu-central-1c'
eb create poke-eb-env

2)
cat /Users/1000geeks/.aws/config
>>> [profile eb-cli]
>>> aws_access_key_id = AKIASBKR2UWDPVFNX3PL
>>> aws_secret_access_key = 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

eb init --profile eb-cli
eb create poke-eb-env


export AWS_ACCESS_KEY_ID="AKIASBKR2UWDPVFNX3PL"
export AWS_SECRET_ACCESS_KEY="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"
export AWS_DEFAULT_REGION="eu-central-1c"
eb init
eb create poke-eb-project