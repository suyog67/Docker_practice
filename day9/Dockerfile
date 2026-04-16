FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

LABEL maintainer="yourname@email.com"
LABEL version="1.0"

CMD ["python" ,"app.py"]
