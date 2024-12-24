# Stage 1: Build and install dependencies
FROM python:3.13-slim-buster AS build

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

# Stage 2: Run tests
FROM build AS test

WORKDIR /app

RUN pytest --verbose

# Stage 3: Build production image
FROM python:3.13-slim-buster AS production

WORKDIR /app

COPY --from=build /app/requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY --from=build /app/app .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]