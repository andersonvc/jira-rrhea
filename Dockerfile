FROM python:3.8.5-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r ./requirements.txt

COPY ./src/backend .
COPY ./src/frontend/assets ./src/frontend/assets
COPY ./src/frontend/templates ./src/frontend/templates

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]