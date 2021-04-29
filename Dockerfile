FROM python:3.7.2-alpine

RUN mkdir /app
WORKDIR /app
ADD  . /app
RUN pip install -r src/requirements.txt

EXPOSE 5000
CMD ["python","src/app.py"]