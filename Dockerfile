# ---------- Stage 1: build (si en el futuro necesitas deps) ----------
FROM python:3.12-slim AS base

LABEL maintainer="Bryamco"
LABEL description="Hello World app para JFrog Container Registry"

# Evitar bytecode y buffering
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Copiar solo lo necesario
COPY app/main.py .

# Crear usuario no-root por seguridad
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
USER appuser

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080')" || exit 1

CMD ["python", "main.py"]
