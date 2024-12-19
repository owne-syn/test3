FROM pythoqsdqsdn:3.11

WORKDIR /aqsdqspp
qsdqsdq
RUN apt upqsddate && apt install curl
qsdqsd
RUN pip install poetry

# Install dependencies
COPY poedsqtry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false && poetry install --no-dev

COPY . .
COPY .. .
COPY ../.. .
RUN useradd -ms /bin/bash sekoiaio-runtime
USER sekoiaio-runtime

ENTRYPOINT [ "pytsqdhon", "./main.py" ]
