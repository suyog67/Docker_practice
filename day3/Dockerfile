
FROM python:3.11


WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY . .

ENV APP_NAME=MyDockerApp
ENV APP_ENV=production


EXPOSE 5000

CMD ["python", "app.py"]
