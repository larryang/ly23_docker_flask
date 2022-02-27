# Project Setup

[![Production Workflow](https://github.com/larryang/ly23_docker_flask/actions/workflows/prod.yml/badge.svg)](https://github.com/larryang/ly_docker_flask/actions/workflows/prod.yml)

* [Production Deployment](https://ly23-prod.herokuapp.com/)


[![Development Workflow](https://github.com/larryang/ly23_docker_flask/actions/workflows/dev.yml/badge.svg)](https://github.com/larryang/ly_docker_flask/actions/workflows/dev.yml)

* [Developmental Deployment](https://ly23-dev.herokuapp.com/)

## Setting up CI/CD

When creating a pull request to merge a branch to master, GitHub will deploy to Heroku development app/dyno.  When merging or pushing to master on GitHub, it will deploy the app to the production Heroku app/dyno.

## Running Locally

1. To build with docker compose:
   docker compose up --build
2. To run tests, Lint, and Coverage report use this command: pytest --pylint --cov

.pylintrc is the config for pylint .coveragerc is the config for coverage setup.py is a config file for pytest


### Future Notes and Resources
* https://flask-user.readthedocs.io/en/latest/basic_app.html
* https://hackersandslackers.com/flask-application-factory/
* https://suryasankar.medium.com/a-basic-app-factory-pattern-for-production-ready-websites-using-flask-and-sqlalchemy-dbb891cdf69f
