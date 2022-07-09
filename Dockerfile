FROM python

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 8000
ARG DJANGO_MEDIA_ROOT=/app/media/store
ARG DJANGO_STATIC_ROOT=/app/staticfiles 
ENTRYPOINT [ "python","manage.py","runserver"]
CMD [ "0.0.0.0:8000" ]
