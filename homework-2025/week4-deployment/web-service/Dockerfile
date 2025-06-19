FROM python:3.12-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY ["pyproject.toml","uv.lock", "./"]

# Install dependencies
RUN uv sync --frozen --no-cache

# Copy the application code
COPY ["predict.py", "model.bin", "./"]

EXPOSE 9696

# Run the application
ENTRYPOINT ["/app/.venv/bin/gunicorn","--bind=0.0.0.0:9696", "predict:app"]