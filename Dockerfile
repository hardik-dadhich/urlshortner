FROM python:3.8

ADD . /urlshortener

WORKDIR /urlshortener

RUN pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv shell && pipenv install
EXPOSE 8000 

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000"]