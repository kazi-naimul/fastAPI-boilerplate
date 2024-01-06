# Welcome to FastAPI Boilerplate

Ready to kickstart your FastAPI project? Look no further! This boilerplate offers you a robust foundation for building powerful applications.

## Key Highlights

✅ Docker Compose for seamless production setup. \
✅ Local Dockerized database for convenient development. \
✅ PgAdmin Docker container for easy database inspection. \
✅ Migrations, Serializers, and ORM configurations ready to roll. \
✅ Token Authentication for secure endpoints. \
✅ Logging Mechanism for effective debugging. \
✅ Pytest for Test-Driven Development (TDD). \
✅ Separate SQLite database and mock sessions for testing. \
✅ Poetry for hassle-free dependency management and packaging.

## Powered by These Technologies

- **Alembic:** Simplifying database migrations.
- **SQLAlchemy:** Trustworthy ORM capabilities.
- **Pydantic:** Handling typing and serialization with ease.
- **Pytest:** Empowering Test-Driven Development (TDD).
- **Poetry:** The smarter choice for dependency management.
- **Docker & docker-compose:** Virtualization for efficient development.
- **PostgreSQL:** A robust relational database system.
- **PgAdmin:** Your ally for efficient database management.
- **Loguru:** The simplest logging solution.

## Quick Setup

1. Create a `.env` file in the root folder (`fastapi-boilerplate/.env`):

    ```env
    DATABASE_URL=postgresql+psycopg2://postgres:password@db:5432/boiler_plate_db
    DB_USER=postgres
    DB_PASSWORD=password
    DB_NAME=boiler_plate_db
    PGADMIN_EMAIL=admin@admin.com
    PGADMIN_PASSWORD=admin
    X_TOKEN=12345678910
    ```

2. Launch Docker Compose:

    ```bash
    docker-compose up
    ```

## 🎉 Get started with your FastAPI CRUD backend at `localhost:8000`.

- Discover Swagger docs at `localhost:8000/docs`.
- Dive into PgAdmin at `localhost:5050`.

Feel free to tailor and tweak this boilerplate to suit your FastAPI project needs!

# Acknowledgments
A big shoutout to the original <a href="https://github.com/rawheel/fastapi-boilerplate">rawheel/fastapi-boilerplate</a> for providing the initial inspiration. The foundation laid by the original repository has been instrumental in shaping this customized boilerplate.