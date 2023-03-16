ARG RUNTIME_VERSION="3.11.1"
FROM python:${RUNTIME_VERSION}
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1
WORKDIR /{{cookiecutter.workdir}}
RUN pip install --upgrade pip && pip install poetry
COPY application/pyproject.toml ./
RUN poetry install
