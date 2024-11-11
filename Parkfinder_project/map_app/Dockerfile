FROM continuumio/miniconda3

LABEL maintainer="O'brien"

RUN apt-get -y update && apt-get -y upgrade && apt-get -y install software-properties-common certbot python3-certbot-nginx

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=CA1.settings

RUN mkdir -p /app
WORKDIR /app

# Create the environment:
COPY ENV.yml .
RUN conda env create -f ENV.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "awm_env", "/bin/bash", "-c"]

# Copy everything in your Django project to the image.
COPY ../manage.py /app/manage.py
ENV PYTHONPATH="/app"

COPY ../docker-entrypoint.sh /app/docker-entrypoint.sh
# Ensure the entrypoint script is executable
RUN chmod +x /app/docker-entrypoint.sh

ENTRYPOINT ["/app/docker-entrypoint.sh"]

# Exposing the port that the container will operate feel free to change is port is taken
EXPOSE 8000

CMD ["uwsgi", "--ini", "/app/uwsgi.ini"]