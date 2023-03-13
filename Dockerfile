FROM python:3.9-alpine
WORKDIR /poke-api
COPY ./ /poke-api/
# RUN apl update && pip install -r /poke_api/poke-api/requirements.txt --no-cache-dir
RUN apl update && pip install -r /poke-api/poke_api/requirements.txt --no-cache-dir
# указьіваю что будем работат с портом 8000
EXPOSE 8000

# CWD ["python3", "/poke-api/poke_api/manage.py", "runserver", "0.0.0.0:8000"]
CWD ["python", "/poke_api/manage.py", "runserver", "0.0.0.0:8000"]






