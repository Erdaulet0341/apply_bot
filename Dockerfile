# Description: Dockerfile for the python application, python:3.9-slim  is easy to use and
# has a smaller image size compared to python:3.9.
FROM python:3.9-slim
WORKDIR /code
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD ["bash", "-c", "python main.py"]
