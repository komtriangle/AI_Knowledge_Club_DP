FROM python:3.9
 
WORKDIR /code
 
COPY ./requirements.txt /code/requirements.txt

RUN apt-get update && apt-get install -y default-jdk
 
RUN pip install -r /code/requirements.txt
 
COPY . /code

CMD ["python", "main.py"]