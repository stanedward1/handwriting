FROM python:3.8
WORKDIR /handwritingapi/handwritingapi

COPY requirements.txt ./
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY .. .
ENV LANG C.UTF-8

CMD ["gunicorn", "mydjango.wsgi:application","-c","./gunicorn.conf.py"]