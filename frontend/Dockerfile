FROM python:3.12-slim

WORKDIR /frontendapp

COPY . /frontendapp

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","app.py"]