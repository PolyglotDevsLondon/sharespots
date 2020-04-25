FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi \
  # Translations dependencies
  && apk add gettext \
  # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
  && apk add postgresql-client \
  && apk add bash \
  # install Node.js & npm
  && apk add --update nodejs nodejs-npm

RUN node -v
RUN npm -v

COPY ./frontend/package.json /package.json
RUN npm install

RUN apk add py-zmq libxml2-dev libxslt-dev g++

#RUN apk add gcc python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev g++
RUN pip install --upgrade pip

RUN addgroup -S django \
  && adduser -S -G django django
#RUN apk del .build-deps gcc musl-dev

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./compose/local/django/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint
RUN chown django /entrypoint

COPY ./compose/local/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start


WORKDIR /app

ENTRYPOINT ["/entrypoint"]
