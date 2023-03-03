FROM python:3.10.2-alpine

WORKDIR /app
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app
COPY requirements.txt .


RUN pip install -r requirements.txt
COPY . .
RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
