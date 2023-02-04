ARG RUNTIME_VERSION="3.11.1"
FROM python:${RUNTIME_VERSION}
WORKDIR /{{cookiecutter.workdir}}
RUN pip install --upgrade pip && pip install poetry
COPY application/pyproject.toml ./
RUN poetry install