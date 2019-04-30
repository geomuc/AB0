FROM bitnami/nginx:latest

RUN mkdir /app/www
RUN mkdir /app/www/html 
RUN mkdir /app/www/html/private
RUN mkdir /app/www/html/private/dist
#    mkdir /home/swuser/app 
#    groupadd -r swuser -g433 && \
#    useradd -u 431 -r -g swuser -d /home/swuser -s /sbin/nologin -c "Docker image user" swuser && \
#    chown -R swuser:swuser /home/swuser && \
#    chown -R swuser:swuser /home/swuser/app 


#EXPOSE 8080
EXPOSE 8080

# RUN nginx
#EXPOSE 443

#USER swuser

WORKDIR /app/www/html
COPY index.html /app/www/html/private
COPY dist /app/www/html/private/dist
COPY nginx.conf /opt/bitnami/nginx/conf

