### River Flow Rate Tracker

---

This example application covers using Timescale DB functions to produce a useable API based on river flow for some local rivers around me in the UK. Data for the last 3 months (11/2020 - 01/2021) is sourced from https://environment.data.gov.uk/hydrology.

Getting Started

An instance of TimescaleDB with Postgis is deployed using Docker.

```sh
docker-compose up
```

Open a new shell and cd into src

```sh
python manage.py load-sample
python manage.py runserver
```
