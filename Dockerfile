FROM python:3.9-alpine
WORKDIR /poke-api
# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY ./ /poke-api/
# RUN apl update && pip install -r /poke_api/poke-api/requirements.txt --no-cache-dir
# RUN apk update && apk add --no-cache mariadb-connector-c-dev && pip install --upgrade -r /poke-api/poke_api/requirements.txt --no-cache-dir
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev && pip install --upgrade -r /poke-api/poke_api/requirements.txt --no-cache-dir
# указьіваю что будем работат с портом 8000
EXPOSE 8000


# CWD ["python3", "/poke-api/poke_api/manage.py", "runserver", "0.0.0.0:8000"]
# CWD ["python", "/poke_api/manage.py", "runserver", "0.0.0.0:8000"]
CMD ["python3", "/poke_api/manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["python3", "/poke-api/poke_api/manage.py", "runserver", "0.0.0.0:8000"]




