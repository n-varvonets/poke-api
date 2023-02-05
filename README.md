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