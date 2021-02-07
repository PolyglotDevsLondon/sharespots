# Sharespots

Sharespots is a simple Django app that displays a curated list of cafes/co-working spaces to meetup and work in London.

<!--
@TODO Add auto table of contents after this issue is fixed
https://github.com/isaacs/github/issues/215
e.g. [TOC] or {:toc max_level=3 }
-->

## Technology Stack

- Backend: Python & Django
- Front-end: SASS/HTML5/JavaScript
- Hosting: Heroku
- Storage: AWS S3

## Tests

We use [pytest](https://docs.pytest.org/en/stable/) for our tests
Run the tests with `pytest`

## Software Tools Required

1. **Terminal**: [iTerm2](https://www.iterm2.com/) (MacOSX), [Terminator](http://gnometerminator.blogspot.co.uk/p/introduction.html) (Linux) or use your preferred one.
2. **Text Editor**: [Sublime Text](http://www.sublimetext.com/) or your preferred one.
3. [Docker Desktop](https://www.docker.com/products/docker-desktop)
4. [Node.js](https://nodejs.org/en/)


## Getting started

Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop) if you haven't already.

 If you are NOT using a Mac (e.g. you are using Windows or Linux) then install [Docker Compose](https://docs.docker.com/compose/install/).

Download and install [Node.js](https://nodejs.org/en/) if you haven't already.

Open [iTerm2](https://www.iterm2.com/) (or your preferred terminal.)

Clone the repo:

```shell
git clone git@github.com:PolyglotDevsLondon/sharespots.git
```

Change directory into the sharespots directory:

```shell
cd sharespots
```

### Quick setup using scripts

Run the this command to set up the project

```
npm run bootstrap
```

Then run this command to launch the back-end
```
npm run dev:docker
```

Open a new iTerm2 terminal tab by pressing ⌘T (or open an additional terminal window using your preferred terminal.)

Run this command to launch the back-end:
```
npm run dev
```

If this worked then you do not need to do manual setup.

If this didn't work  look at the [troubleshooting](#Troubleshooting) section.

(You may, or may not, need to [add opencage api [add opencage api key](###Add-opencage-api-key) - @TODO test this and update instructions.)

If it still isn't working try the longer manual setup below.

### Longer manual setup

Build the docker container (included is django, postgres, pgadmin and jupyter notebook run from django_extensions):

```shell
docker-compose -f local.yml build
```

Launch the docker container:
```shell
docker-compose -f local.yml up
```

Open project in your web browser at:

[http://0.0.0.0:8000/](http://0.0.0.0:8000/)

You should now see the Sharespots website (but no venue data will show yet.)

Open a new iTerm2 terminal tab by pressing ⌘T (or open an additional terminal window using your preferred terminal.)

Change to your sharespots directory:

```shell
cd [your/sharespot/directory]
```

Load seed data:

```shell
docker-compose -f local.yml run django python manage.py loaddata seed_data.json
```

Set up a super user for django admin:

```shell
docker-compose -f local.yml run django python manage.py createsuperuser
```

Build everything frontend related

```
run npm i && npm run build 
```

Reload your project in your web browser at

[http://0.0.0.0:8000/](http://0.0.0.0:8000/)

**You should now see the Sharespots website with venues displaying.**

(Optional) Open another browser tab/window and login using the superuser account you created in the django admin panel at [http://0.0.0.0:8000/admin](http://0.0.0.0:8000/admin)

Continuously monitor front end changes

```
npm run dev
```

## Troubleshooting



### Rebuild your docker container

If the project doesn't work after pulling the latest changes by doing a `git pull`, you may need to rebuild to include recently added python modules:

```shell
docker-compose -f local.yml build
```

### Add opencage api key

[Create an OpenCage API key](https://opencagedata.com/)

And add your OpenCage API key to sharespots/.env/.local/.django e.g.:

```
# General
# ------------------------------------------------------------------------------
USE_DOCKER=yes
IPYTHONDIR=/app/.ipython


SECRET_KEY=[secret key]
OPENCAGE_API_KEY=[opencage_api_key]
DJANGO_DEBUG=True
ALLOWED_HOSTS=['*']

```

## Useful Database commands

### Make migrations

```shell
docker-compose -f local.yml run django python manage.py makemigrations
```

### Load data from seed file
```
docker-compose -f local.yml run django python manage.py dumpdata core.venue > core/fixtures/seed_data.json
```

### Dump data to seed file

To export the Sharespots data from a database to a file:

```
docker-compose -f local.yml run django python manage.py dumpdata core.venue > core/fixtures/seed_data.json
```

Then remove auth data at the top to leave just core models.


## Useful Front End commands

### Install front end dependencies

To install third party libraries:

```
npm i
```
### Build front-end once
To build everything frontend related run `npm run build`

This will build the front-end files (e.g. css styling files) once.

### Build front-end continuously

When developing continuously monitor front-end files and rebuild  whenever files changed:

```
npm run dev
```

## Useful Heroku commands

Command to create a superuser in **staging**:

```console
heroku run python manage.py createsuperuser --app sharespots-app
```

Command to create a superuser in staging **production**:

```console
heroku run python manage.py createsuperuser --app sharespots-prod
```

## Team

### Current

- [Lili](https://github.com/lili2311)
- [Simon](https://github.com/simonRedwards)
- [Tsveti](https://github.com/tsvetelinak0)
- [Chris Wedgwood](https://github.com/chriswedgwood)
- [Louie Christie](https://github.com/louiechristie)
- [Ravi Pullagurla](https://github.com/ravinderreddy-p)
- [Abu Darda](https://github.com/abuDarda97)

### Previously contributed

- [Kit Sum Pang](https://github.com/ktsmpng)
- [Ju-Vern](https://github.com/juvern)
- [Maurice](https://github.com/mbanerjeepalmer)
- [Stefano](https://github.com/CianciuStyles)
- [Fatimat](https://github.com/gbaja)
- [Dan](https://github.com/snowkuma)
- [Adnan](https://github.com/adnansalehin)
- [Thao Vo](https://github.com/littlethao)
- [Andreea](https://github.com/etiquetteX)
