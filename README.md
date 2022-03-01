## About
This is the simple example of blog using `FastAPI` framework with `SQLAlchemy` asynchronous ORM
## Local run
Next environment variables used are specified in `.env` file:
* `DATABASE_URL_SYNC` - database url in sync mode. Alembic uses it to control tables version and push migrations
* `DATABASE_URL_ASYNC` - database url in async mode. Used by SQLAlchemy to create engine and work with async sessions
* `SECRET_KEY` - app secret key. JWT tokens signing
* `JWT_ALGORITHM` - jwt encode-decode algorithm
* `EMAIL_HOST_NAME` - email for emails be sent from
* `EMAIL_HOST_PASSWORD` - email password (use Google specific app password)

### Start app
- `docker-compose up`

### Run alembic revision (make migrations)
- `docker-compose run web alembic revision --autogenerate -m "Commit message"`
### Run alembic upgrade (migrate)
- `docker-compose run web alembic upgrade head`