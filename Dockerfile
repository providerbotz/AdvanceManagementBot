FROM python:3.10-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
WORKDIR /AutoFilterBot   #Add Your Repo Name After Fork If You Not Change Name At Fork Time Then You Not To Change It Otherwise Change..

COPY . .

CMD python3 -m Provider ##Do Not Change It
