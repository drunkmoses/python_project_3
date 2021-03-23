FROM python:3.7-alpine
WORKDIR /app
COPY *.py /app
RUN pip install requirements.txt
EXPOSE 5000
VOLUME /app/logs
