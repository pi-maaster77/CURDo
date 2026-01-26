FROM python:3.11-slim

WORKDIR /app

# Copiar requirements e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar la aplicación
COPY . .

# Comando para ejecutar la app
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "main:app"]
