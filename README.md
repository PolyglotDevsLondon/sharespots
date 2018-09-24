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
6. [Setup Postgres database locally](##Database(postgres))
7. Apply the initial database migrations: `python manage.py migrate`

## Running the project locally
0. If not already active, activate the virtual environment: `workon sharespots`
1. Run `python manage.py runserver`
2. Open your browser at http://localhost:8000/


## Front End changes
_todo_

# Contributing
Please follow the [Contributing Guidelines](CONTRIBUTING.md)

## Database(postgres)

### Mac OSX

Download and install Postgres using https://postgresapp.com/.
Once you have installed click initialise
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

```
psql (10.5)
Type "help" for help.

_username_=#
```

Create a new database called listings

<pre>
# CREATE DATABASE listings;
# CREATE ROLE listings WITH LOGIN PASSWORD '<i>your password not this</i>';
# GRANT ALL PRIVILEGES ON DATABASE listings TO listings;
# ALTER USER listings CREATEDB;
</pre>



