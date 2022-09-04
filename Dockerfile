FROM debian:latest



RUN apt update && apt upgrade -y

RUN apt install git curl python3-pip ffmpeg -y

RUN pip3 install -U pip

RUN cd /

RUN git clone https://github.com/hackerheroOP/VideoMerge-Bot4

RUN cd VideoMerge-Bot4

WORKDIR /VideoMerge-Bot4

RUN pip3 install -U -r requirements.txt

CMD python3 main.py
