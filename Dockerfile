FROM python:3.8-slim

WORKDIR /app

ADD ./ /app/

RUN pip install --upgrade pip && \
	pip install -r /app/requirements.txt

ENV FLASK_ENV=development
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

#CMD gunicorn -b "0.0.0.0:8000" --timeout 900 app:app
CMD flask run --cert=adhoc

VOLUME /app
