FROM python:latest

COPY . .

RUN pip install -r requirements.txt

WORKDIR /churchcontact

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000
