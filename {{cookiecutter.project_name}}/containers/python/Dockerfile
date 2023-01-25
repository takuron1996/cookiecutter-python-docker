ARG RUNTIME_VERSION="3.11.1"
FROM python:${RUNTIME_VERSION}
WORKDIR /{{cookiecutter.workdir}}
ENV TZ="Asia/Tokyo"
RUN echo $TZ > /etc/timezone
ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry

