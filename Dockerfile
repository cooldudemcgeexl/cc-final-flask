FROM python:slim

WORKDIR /home/app

COPY 'requirements.txt' ./ 

COPY 'entry_script.sh' ./

RUN apt update && apt install build-essential -y

RUN pip install -r requirements.txt

COPY final/ ./


CMD ["/home/app/entry_script.sh"]
