FROM python:3.13.0-slim

ENV USER=uv-example-user \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_PROJECT_ENVIRONMENT=/usr/local

RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -m -s /bin/bash $USER

COPY --from=ghcr.io/astral-sh/uv:0.5.5 /uv /uvx /bin/

ENV APP_DIR=/home/$USER/src
WORKDIR $APP_DIR

RUN --mount=type=cache,target=/home/$USER/.cache/uv \
    --mount=type=bind,source=src/uv.lock,target=uv.lock \
    --mount=type=bind,source=src/pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project

COPY src $APP_DIR

RUN --mount=type=cache,target=/home/$USER/.cache/uv \
    uv sync --frozen

ENV PYTHONPATH=$APP_DIR

RUN chown -R "$USER":"$USER" $APP_DIR
USER $USER

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
