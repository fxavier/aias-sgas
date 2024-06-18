# Use a specific version of the python image for consistency
FROM python:3.9-alpine3.13

LABEL maintainer="xavierfrancisco353@gmail.com"

ENV PYTHONUNBUFFERED 1

# Copying requirements first to leverage Docker cache
COPY ./requirements.txt /requirements.txt
COPY ./app /app
COPY ./scripts /scripts

WORKDIR /app

EXPOSE 8000

# Install dependencies in a single RUN command to reduce layers
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache \
      postgresql-client \
      gcc \
      libc-dev \
      make \
      git \
      libffi-dev \
      openssl-dev \
      python3-dev \
      libxml2-dev \
      libxslt-dev \
      build-base \
      postgresql-dev \
      musl-dev \
      linux-headers && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home app && \
    # Clearing APK cache
    rm -rf /var/cache/apk/*

# Setting up application directories
RUN mkdir -p /vol/web/static /vol/web/media && \
    chown -R app:app /vol /app && \
    chmod -R 755 /vol/web && \
    chmod -R 777 /py/* && \
    chmod +x /scripts/*


#ENV PATH="/py/bin:$PATH"
ENV PATH="/scripts:/py/bin:$PATH"

USER app

CMD ["run.sh"]