FROM python:3.12-slim

WORKDIR /userapp

COPY . /userapp

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","app.py"]