FROM python:3.10-slim

# Install system dependencies for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt

# Upgrade pip to the latest version
RUN python -m pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir -r /code/requirements.txt
COPY ./app /code/app

EXPOSE 8000
CMD [ "uvicorn", "app.server1:app", "--host", "0.0.0.0", "--port", "8000" ]