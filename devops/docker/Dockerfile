FROM python:3.10.4-bullseye AS venv

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

ENV PATH /root/.poetry/bin:$PATH

WORKDIR /app
COPY fastapi-server/pyproject.toml fastapi-server/poetry.lock ./
RUN python -m venv --copies /app/venv
RUN . /app/venv/bin/activate && poetry install  --no-dev && pip uninstall pip -y

FROM python:3.10.4-slim-bullseye as prod

COPY --from=venv /app/venv /app/venv

RUN pip uninstall pip -y

ENV PATH /app/venv/bin:$PATH

WORKDIR /app
COPY ./fastapi-server/app ./app
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
