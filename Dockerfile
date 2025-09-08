FROM python:3.11-slim


WORKDIR /app


COPY . /app


RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        awscli \
        build-essential \
        libpq-dev \
        curl && \
    rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000


EXPOSE 8000

CMD ["python3", "app.py"]

