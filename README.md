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

## Project Setup

Open iTerm2 (or your preferred terminal.)

Clone the repo:

```shell
git clone git@github.com:PolyglotDevsLondon/sharespots.git
```

Change directory into the sharespots directory:

```shell
cd sharespots
```

[Download and install Docker Desktop](https://www.docker.com/products/docker-desktop) if you haven't already.

Build the docker container (included is django, postgres, pgadmin and jupyter notebook run from django_extensions):

```shell
docker-compose -f local.yml build
```

[Create your an OpenCage API key](https://opencagedata.com/)

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

Fire up the docker container:

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

Reload your project in your web browser at

[http://0.0.0.0:8000/](http://0.0.0.0:8000/)

**You should now see the Sharespots website with venues displaying.**

(Optional) Open another browser tab/window and login using the superuser account you created in the django admin panel at [http://0.0.0.0:8000/admin](http://0.0.0.0:8000/admin)

For the OpenCage api you would need to create your own API key.
[Click here](https://opencagedata.com/) to make one.

## Front End changes

1. To install [Sass](https://sass-lang.com/install)

   - You can install using node package manager `docker-compose -f local.yml run npm install -g sass`
   - Windows: `choco install sass`
   - Mac OS X: `brew install sass/sass/sass`

2. To build everything frontend related run `npm i && npm run build`

## Troubleshooting

If the project doesn't work after pulling the latest changes by doing a `git pull`, you may need to:

### Rebuild your container to include recently added python modules

```shell
docker-compose -f local.yml build
```

### Run new database migrations

```shell
docker-compose -f local.yml run django python manage.py makemigrations
```

### Update Seed data

To export the Sharespots data from a database to a file:

```
docker-compose -f local.yml run django python manage.py dumpdata core.venue > core/fixtures/seed_data.json
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
