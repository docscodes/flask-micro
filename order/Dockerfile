FROM python:3.12-slim

WORKDIR /orderapp

COPY . /orderapp

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","app.py"]