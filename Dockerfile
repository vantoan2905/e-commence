FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /recomment_product

COPY ./requirements.txt /recomment_product/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /recomment_product/

CMD ["sh", "-c", "python manage.py makemigrations && \
                   python manage.py migrate && \
                   python manage.py load_data && \
                   python manage.py render_User && \
                   python manage.py runserver "]
