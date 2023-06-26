FROM ubuntu:latest
RUN apt-get update
RUN apt-get -y install apache2
RUN apt-get -y install systemctl
COPY index.html /var/www/html
EXPOSE 80
ENTRYPOINT ["systemctl", "start"]
CMD ["apache2"]

