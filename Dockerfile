FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DATA_PATH=/app/data/ML_Lucknow.csv

CMD ["python", "main.py"]
