# Dockerizing Django Application

This repository contains a Dockerfile and docker-compose.yml file to Dockerize a Django application.

## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started
```bash
Add the Csv files to the path like => backend_assessmnet/School_app/Ganison_dataset/1.csv
```
### 1. Clone the Repository:

```bash
git clone https://github.com/Asam8385/Csv_reader_django.git
```


### 2. Build the Docker containers:
```bash
docker-compose build
```

### 3. Run the migrations:
```bash
docker-compose run web python manage.py migrate
```

```
Access the Django development server at http://localhost:8000.








