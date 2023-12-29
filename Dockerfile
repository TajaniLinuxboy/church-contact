FROM python:latest

COPY . .

WORKDIR /contactapp

RUN python install -r requirements.txt

CMD ["flask", "run", "-p", "5000"]

EXPOSE 5000
