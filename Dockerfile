FROM python:3.11.3

WORKDIR /myapp

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /myapp/requirements.txt

# dependencies
RUN pip install --upgrade pip setuptools wheel \
    && pip install -r requirements.txt \
    && rm -rf /root/.cache/pip

COPY ./ /myapp

ENTRYPOINT [ "streamlit", "run", "app/main.py", "--server.port=8080", "--server.address=0.0.0.0" ]
