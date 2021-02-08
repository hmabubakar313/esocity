FROM python:3.7-slim
ENV PYTHONUNBUFFERED=1
WORKDIR  /esociety
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY manage.py ./manage.py
COPY esociety ./esociety
EXPOSE 8000