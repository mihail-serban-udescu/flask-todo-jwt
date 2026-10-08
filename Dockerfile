# Imaginea de bază: Python 3.12 slim (ușoară)
FROM python:3.12-slim

# Setăm directorul de lucru în container
WORKDIR /app

# Variabile de mediu pentru Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalăm dependențele sistemului (pentru bcrypt)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiem requirements.txt și instalăm dependențele Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiem restul codului
COPY . .

# Expunem portul 5000
EXPOSE 5000

# Comanda de pornire
CMD ["python", "run.py"]