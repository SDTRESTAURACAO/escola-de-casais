# Usando Python 3.12 como base
FROM python:3.12

# Define diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . .

# Instala dependências do Flask
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta do app
EXPOSE 8080

# Comando para rodar o Flask usando Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
