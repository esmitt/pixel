# --- Stage 1: Install dependencies and run tests ---
FROM python:3.13-slim AS test

WORKDIR /pixel/backend

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

# Run tests using the pytest.ini configuration
RUN pytest --verbose

# --- Stage 2: Build the production image ---
FROM python:3.13-slim

WORKDIR /pixel/backend

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY app ./app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
