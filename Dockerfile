# 
FROM python:3.9

# 
WORKDIR /app

# 
COPY ./requirements.txt /app/requirements.txt
COPY ./alembic.ini /app/alembic.ini
# 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# 
COPY . /app

# 
CMD ["fastapi", "run", "main.py", "--port", "8001"]   