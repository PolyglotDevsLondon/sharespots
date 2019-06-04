# Sharespots

Simple Django app that displays a list of curated cafes/spaces to meetup and work in London

# Content

1. [Description](#description)
2. [Setup](#setup)
3. [Contributing](#contributing)

# Description

## Tech

- Backend: Python & Django
- Front-end: SASS/HTML5/JavaScript
- Hosting: Heroku
- Storage: AWS S3

## Team

- [Lili](https://github.com/lili2311)
- [Fatimat](https://github.com/gbaja)
- [Maurice](https://github.com/mbanerjeepalmer)
- [Stefano](https://github.com/CianciuStyles)
- [Simon](https://github.com/simonRedwards)
- [Dan](https://github.com/snowkuma)
- [Kit Sum Pang](https://github.com/ktsmpng)
- [Ichi](https://github.com/icicleta)
- [Tsveti](https://github.com/tsvetelinak0)
- [Amy Boyd](https://github.com/amyboyd)
- [Chris Wedgwood](https://github.com/chriswedgwood)
- [Thao Vo](https://github.com/littlethao)
- [Andreea](https://github.com/etiquetteX)
- [Adnan](https://github.com/adnansalehin)
- [Ju-Vern](https://github.com/juvern)
- [Louie Christie](https://github.com/louiechristie)

# Setup

## Tools

1. **Terminal**: [iTerm2](https://www.iterm2.com/) (MacOSX), [Terminator](http://gnometerminator.blogspot.co.uk/p/introduction.html) (Linux) or use your preferred one.
2. **Text Editor**: [Sublime Text](http://www.sublimetext.com/) or you preferred one.

Install virtualenv: pip install virtualenv
Install virtualenvwrapper: pip install virtualenvwrapper \*You can skip this and use virtualenv installed in a step before directly, virtualenvwrapper allows for nice interfacing with virtualenv
Source the virtualenvwrapper: source /usr/local/bin/virtualenvwrapper.sh NOTE: To help do this automatically on every new shell you open add the line above to your .bash_profile or .bashrc
Create a new env for the project: mkvirtualenv pimp

## Laptop Setup

1. [Setup](https://github.com/PolyglotDevsLondon/setup/wiki)

## Virtual Enviroment Setup

This allows you to install all the Python dependencies in a "box" so they are not globally installed and clashing with other projects.

1. Install [virtualenv](https://virtualenv.pypa.io/en/stable/):
   `pip install virtualenv`
2. Install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html):
   `pip install virtualenvwrapper`
   \*You can skip this and use [virtualenv](https://virtualenv.pypa.io/en/stable/) installed in a step before directly, virtualenvwrapper allows for nice interfacing with virtualenv
3. Source the `virtualenvwrapper`:
   `source /usr/local/bin/virtualenvwrapper.sh`
   **NOTE**: To help do this automatically on every new shell you open add the line above to your `.bash_profile` or `.bashrc`
4. Create a new env for the project:
   `mkvirtualenv sharespots`

# Project Setup

2. Clone the repo: `git@github.com:PolyglotDevsLondon/sharespotsgit`
3. Create a new virtual environment with virtualenvwrapper: `mkvirtualenv -a sharespots sharespots`
4. `cd` into the `sharespots` folder
5. Install all the dependencies: `pip install -r requirements.txt`
6. [Setup Postgres database locally](#database)
7. Apply the initial database migrations: `python manage.py migrate`

## Running the project locally

0. If not already active, activate the virtual environment: `workon sharespots`
1. Run `python manage.py runserver`
1. Open your browser at http://localhost:8000/

## Front End changes

1. To install [Sass](https://sass-lang.com/install)

- You can install using node package manager `npm install -g sass`
- Windows: `choco install sass`
- Mac OS X: `brew install sass/sass/sass`

2. To build everything Front end related run `npm run build`

# Contributing

Please follow the [Contributing Guidelines](CONTRIBUTING.md)

# Database

We are using PostgreSQL 9.5

## Mac OSX

1. Download and install Postgres using https://postgresapp.com.
2. Once you have installed click initialise

### Create a new DB

You have a few options to make a new DB, either:

1. In your command line run `createdb sharespots`
2. Set the DATABASE_URL env variable `export DATABASE_URL=postgresql:///sharespots`

Or create the DB via psql command line:

#### Create a new DB via psql

You should see three databases _yourusername_ postgres and template1

Run this in your terminal:

```
sudo mkdir -p /etc/paths.d &&
echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp
```

This will let you run psql command from anywhere. Either double click on once of the databases in postgresapp
or go to bash and type

```
$ psql
```

You will see something similar to this:

<pre>
psql (10.5)
Type "help" for help.

<i>yourusername</i>=#
</pre>

Create a new database called sharespots.

<pre>
# CREATE DATABASE sharespots;
# CREATE ROLE sharespots WITH LOGIN PASSWORD 'sharespots';

<pre>
psql (10.5)
Type "help" for help.

<i>yourusername</i>=#
</pre>

Create a new database called `sharespots`.

<pre>
# CREATE DATABASE sharespots;
# CREATE ROLE sharespots WITH LOGIN PASSWORD 'sharespots';
# GRANT ALL PRIVILEGES ON DATABASE sharespots TO sharespots;
# ALTER USER sharespots CREATEDB;
</pre>

Before running migrate/runserver you will need to add the environment variable
DATABASE_URL into your system. To do this add a .env file into the root of your project
and add the following two lines:
<pre>

DATABASE_URL=postgres://sharespots:sharespots@localhost:5432/sharespots
SECRET_KEY=<i>Insert random long alphanumeric string</i>
</pre>

then

<pre>

$ ./manage.py migrate

</pre>

### Use Docker

1. Download Docker from https://www.docker.com/products/docker-desktop
2. From the root of your project run

<pre>
docker-compose -f local.yml build
</pre>

3. Then run

<pre>
docker-compose -f local.yml up
</pre>

4. Make sure you dont have any errors :)

Included is django, postgres, pgadmin and jupyter notebook run from django_extensions
