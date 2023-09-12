# Build Stage
FROM python:3.9 as build
WORKDIR /usr/app
RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

# Final Deployment Stage
FROM python:3.9-slim

WORKDIR /app
COPY --from=build /usr/app/venv .
COPY . .

ENV PATH="/app/bin:$PATH"

CMD ["python", "SenKongDao.py"]
