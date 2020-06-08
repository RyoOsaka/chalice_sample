FROM python:3.8-slim-buster

ENV TZ Asia/Tokyo
WORKDIR /data/app

COPY Pipfile  ./

RUN apt update -y \
 && apt install -y \
        npm \
        git 

RUN npm install cdk

RUN pip install pipenv \
 && pipenv install --dev 


#CMD ["tail", "-f", "/dev/null"]
