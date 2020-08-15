FROM python:3.8.5-slim-buster

RUN apt-get update; apt-get install curl vim -y

WORKDIR /backend

COPY ./requirements.txt .
RUN pip install -r ./requirements.txt

COPY ./ .
#COPY ./src/frontend/assets ./src/frontend/assets
#COPY ./src/frontend/templates ./src/frontend/templates

EXPOSE 80

#CMD ["ls","-ahl"]
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "80"]