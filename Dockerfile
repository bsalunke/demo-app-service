FROM python:3.10-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_PREFER_BINARY=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
    && apt-get install -y --no-install-recommends --only-upgrade \
        openssl \
        libssl3 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade "pip==26.0" "setuptools==78.1.1" "wheel==0.46.2" \
        "Cython<3.0"

ARG REQ_FILE=requirements.txt
COPY ${REQ_FILE} requirements.txt

RUN grep -vE '^\s*(#|$)' requirements.txt | while read -r pkg; do \
        pip install --prefer-binary --no-cache-dir \
            --use-deprecated=legacy-resolver \
            --ignore-requires-python \
            --no-build-isolation \
            "${pkg}" \
            || echo "SKIP: ${pkg} (could not install)"; \
    done

COPY . .

RUN useradd --create-home --shell /bin/bash app && chown -R app:app /app
USER app

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["python", "app.py"]
