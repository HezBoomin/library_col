FROM python:3.10-bookworm

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    DJANGO_SETTINGS_MODULE=library_col.settings \
    PORT=8000 \
    WEB_CONCURRENCY=2

# Install system packages required Django.
RUN apt-get update --yes --quiet \
    && apt-get install --yes --quiet --no-install-recommends \
    && apt-get install nodejs -y \
    && apt install npm -y --fix-missing \
    && rm -rf /var/lib/apt/lists/* 

RUN addgroup --system django \
    && adduser --system --ingroup django django

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN npm install tailwindcss

# Copy project code
COPY . .

RUN npm run build
RUN python manage.py collectstatic --noinput --clear

# Run as non-root user
RUN chown -R django:django /app
USER django

# Run application
# CMD gunicorn shopping_list.wsgi:application