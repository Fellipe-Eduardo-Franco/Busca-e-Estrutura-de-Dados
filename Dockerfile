FROM python:3.11

WORKDIR /app

COPY . .

CMD ["python", "-m", "unittest", "discover"]
