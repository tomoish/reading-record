# reading-record

![reading-record logo](book_project/reading_record/static/reading_record/images/logo.png)

<!-- [![Technologies Used](https://skillicons.dev/icons?i=python,django,html,css,js,postgres,nginx,docker,aws)](https://skillicons.dev) -->

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,django,html,css,js,postgres,nginx,docker,aws" />
  </a>
</p>

reading-record is a web application for recording your reading contents.

## Web
https://django-reading-record.com

## Technologies Used
- Django 
- PostgresQL
- Nginx

## Production Environment
- AWS EC2

## Usage
### Git clone
```
$ git clone https://github.com/tomoish/reading-record.git
```

### Building a development environment

1. Create .env file in reading-record/book_project directory and set the environment variables:
    ```
    SECRET_KEY=<secret key>
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1,localhost
    DATABASE_URL=postgres://<database user>:<database password>@localhost:/<database name>
    DATABASE_DB=<database name>
    DATABASE_USER=<database user>
    DATABASE_PASSWORD=<database password>
    DATABASE_HOST=db
    DATABASE_PORT=5432
    
    POSTGRES_USER=<database user>
    POSTGRES_PASSWORD=<database password>
    POSTGRES_DB=<database name>

    DATABASE=postgres
    ```
2. Build the images and run the containers:
   ```
   docker compose up -d --build
   ```
3. Run the migrations:
   ```
   docker compose exec web python manage.py migrate --noinput
   ```
4. Collects the static files into STATIC_ROOT:
   ```
   docker compose exec web python manage.py collectstatic --no-input --clear
   ```
5. Test it out at http://localhost:1317.
