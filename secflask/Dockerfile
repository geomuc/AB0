FROM alpine
RUN apk update && \
    apk add python3 && \
    apk add shadow 

RUN pip3 install gunicorn && \
    pip3 install Flask 

RUN mkdir /home/swuser && \
    mkdir /home/swuser/app && \
    groupadd -r swuser -g433 && \
    useradd -u 431 -r -g swuser -d /home/swuser -s /sbin/nologin -c "Docker image user" swuser && \
    chown -R swuser:swuser /home/swuser && \
    chown -R swuser:swuser /home/swuser/app 


EXPOSE 8080
#sEXPOSE 80

# RUN nginx
#EXPOSE 443

USER swuser

WORKDIR /home/swuser/app
COPY . /home/swuser/app

#RUN chmod +x startskript.sh

#CMD /bin/sh startskript.sh
CMD gunicorn -b "0.0.0.0:8080" test:app