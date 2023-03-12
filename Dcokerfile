FROM python:3.9-alpine
WORKDIR /poke-api
COPY ./ /poke-api
RUN apl update && pip install -r /poke_api/poke-api/requirements.txt --no-cache-dir
CWD ["python", "manage.py", "runserver", "0.0.0.0:8000"]