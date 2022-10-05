FROM python:3.10-slim
EXPOSE 8080
ADD ./requirements.txt /
RUN pip install -r /requirements.txt
ARG GATEWAY
ENV GATEWAY=$GATEWAY
ADD . /plugin
ENV PYTHONPATH=$PYTHONPATH:/plugin
ENV PYTHONUNBUFFERED=1
WORKDIR /plugin/services
CMD python services.py