FROM ubuntu:16.04
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3 
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip 
RUN pip3 install flask pymongo 
RUN mkdir /app
RUN mkdir -p /app/data
COPY app.py /app/app.py
ADD data /app/data
EXPOSE 5000
WORKDIR /app
ENTRYPOINT ["python3" , "-u" , "app.py"]
