FROM registry.cn-chengdu.aliyuncs.com/ops-k8s/python:3.8.9-slim

WORKDIR /opt/app

COPY app.py /opt/app
RUN pip install --no-cache-dir tornado

CMD [ "python", "/opt/app/app.py" ]