FROM python:3.12-slim

WORKDIR /bookapp

COPY . /bookapp

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","app.py"]