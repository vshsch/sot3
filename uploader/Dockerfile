FROM python:3.9-slim

WORKDIR /app

COPY upload.py /app/upload.py

RUN pip install minio

CMD ["python3", "upload.py"]
