FROM python:3.11

WORKDIR /app
qsdqsdq
RUN apt update && apt install curl
qsdqsd
RUN pip install poetry

# Install dependencies
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false && poetry install --no-dev

COPY . .
COPY .. .
COPY ../.. .
RUN useradd -ms /bin/bash sekoiaio-runtime
USER sekoiaio-runtime

ENTRYPOINT [ "python", "./main.py" ]
