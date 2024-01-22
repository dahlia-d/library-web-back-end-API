FROM python:3.8

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 5000

ENV NAME App

CMD ["flask","run", "--debug" ,"--host=0.0.0.0", "--port=5000"]