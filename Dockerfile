FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/

# pipは最新版にする
RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install -r requirements.txt
RUN pip install pymysql \
bs4 \
scrapy

# ffmpegの導入
RUN wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz
RUN tar Jxfv ffmpeg-release-amd64-static.tar.xz
RUN cp ./ffmpeg*amd64-static/ffmpeg /usr/local/bin

# GCPのクレデンシャルファイル名を記載する
ENV GOOGLE_APPLICATION_CREDENTIALS /usr/gcp/xxxxxxx.json
# GCPのライブラリ導入
RUN pip install --upgrade google-cloud
RUN pip install --upgrade google-cloud-texttospeech
RUN pip install google-cloud-speech
ADD . /app/
CMD python3 manage.py runserver 0.0.0.0:8000
EXPOSE 8000
