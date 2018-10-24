# Sharespots 
Simple Django app that displays a list of curated cafes/spaces to meetup and work in London

# Content

1. [Description](#description)
4. [Setup](#setup)
5. [Contributing](#contributing)


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

# Setup
## Tools
1. **Terminal**: [iTerm2](https://www.iterm2.com/) (MacOSX), [Terminator](http://gnometerminator.blogspot.co.uk/p/introduction.html) (Linux) or use your preferred one.
2. **Text Editor**: [Sublime Text](http://www.sublimetext.com/) or you preferred one.

# Dev Enviroment Setup

1. [Setup](https://github.com/PolyglotDevsLondon/setup/wiki)
2. Clone the repo: `git@github.com:PolyglotDevsLondon/sharespotsgit`
3. Create a new virtual environment with virtualenvwrapper: `mkvirtualenv -a sharespots sharespots`
4. `cd` into the `sharespots` folder
5. Install all the dependencies: `pip install -r requirements.txt`
6. [Setup Postgres database locally](#database)
7. Apply the initial database migrations: `python manage.py migrate`

## Running the project locally
0. If not already active, activate the virtual environment: `workon sharespots`
1. Run `python manage.py runserver`
2. Open your browser at http://localhost:8000/


## Front End changes
1. To install [Sass](https://sass-lang.com/install) 
- You can install using node package manager `npm install -g sass`
- Windows: `choco install sass`
- Mac OS X: `brew install sass/sass/sass`
2. To compile sass changes to css file use `sass --watch input/file/path/styles.scss output/file/path/styles.css`
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
2. Set the DATABASE_URL env variable `export DATABASE_URL=postgresql://sharespots`

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

Create a new database called listings.

<pre>
# CREATE DATABASE listings;
# CREATE ROLE listings WITH LOGIN PASSWORD '<i>your_password_not_this</i>';

<pre>
psql (10.5)
Type "help" for help.

<i>yourusername</i>=#
</pre>

Create a new database called `sharespots`.

<pre>
# CREATE DATABASE listings;
# CREATE ROLE sharespots WITH LOGIN PASSWORD '<i>your password not this</i>';
# GRANT ALL PRIVILEGES ON DATABASE sharespots TO sharespots;
# ALTER USER listings CREATEDB;
</pre>

Before running migrate/runserver you will need to add the environment variable
DATABASE_URL into your system. 

<pre>

$ export DATABASE_URL=postgres://sharespots:<i>your_password_not_this</i>@127.0.0.1:5432/sharespots

</pre>

then

<pre>

$ ./manage.py migrate

</pre>
