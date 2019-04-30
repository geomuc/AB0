FROM alpine:latest

RUN apk update && \
    apk add python3 && \
    apk add shadow && \
    apk add postgresql-dev && \
    apk add gcc && \
    apk add musl-dev && \
    apk add python3-dev

RUN pip3 install gunicorn && \
    pip3 install Flask && \
    pip3 install flask-sqlalchemy && \
    pip3 install flask-marshmallow && \
    pip3 install flask-cors && \
    pip3 install Flask-Migrate && \
    pip3 install psycopg2


RUN mkdir /home/swuser && \
    mkdir /home/swuser/app && \
    groupadd -r swuser -g433 && \
    useradd -u 431 -r -g swuser -d /home/swuser -s /sbin/nologin -c "Docker image user" swuser 

EXPOSE 8080
#EXPOSE 80
#EXPOSE 443


COPY . /home/swuser/app

RUN chown -R swuser:swuser /home/swuser && \
    chown -R swuser:swuser /home/swuser/app 

USER swuser

WORKDIR /home/swuser/app

#ENTRYPOINT /bin/sh && cd /home/swuser/app && gunicorn -b "0.0.0.0:8080" wsgi &
#ONBUILD COPY . /app
#ONBUILD RUN virtualenv /env && /env/bin/pip install -r /app/requirements.txt


CMD gunicorn -b "0.0.0.0:8080" personapi:app