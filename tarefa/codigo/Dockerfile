#Talles Henrique De Oliveira Nadiceo
#FROM python:3.8-slim
FROM centos/python-36-centos7

COPY . /tarefa

WORKDIR /tarefa

RUN pip install flask  
RUN pip install pandas
RUN pip install fastapi
RUN pip install sklearn
RUN pip install uvicorn[standard]


#ENV FLASK_APP=main.py  

CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "80", "--reload"]
