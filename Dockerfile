FROM ubuntu:14.04


MAINTAINER Foo Bar foo@bar.com
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["readProcess.py"]


