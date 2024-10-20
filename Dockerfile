FROM python:3.11-slim

RUN sed -i "s@http://\(deb\|security\).debian.org@https://mirrors.tuna.tsinghua.edu.cn@g" /etc/apt/sources.list.d/debian.sources && \
    apt-get update && apt-get install -y gnupg2 curl wget unzip ca-certificates ffmpeg

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app

COPY . /app/

# RUN ls -l /app

RUN chmod +x app/start.sh

ENV PYTHONPATH=/app

CMD ["bash", "app/start.sh"]
