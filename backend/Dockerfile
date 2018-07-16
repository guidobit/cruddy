FROM python:3.6-alpine3.6 as base

RUN apk update && \
    apk add --no-cache build-base gcc abuild binutils binutils-doc gcc-doc \
    python3-dev ca-certificates libffi-dev && \
    apk add --no-cache --virtual=build-dependencies tzdata build-base \
    linux-headers && \
    pip3 install --upgrade --no-cache-dir pip && \
    pip3 install --no-cache-dir paho-mqtt requests cffi smbus-cffi && \
    apk del build-dependencies && \
    rm -rf /tmp/* /var/tmp/* /var/cache/apk/*


WORKDIR /app

EXPOSE 8000
CMD python run.py


FROM base as prod
COPY ../ /app

COPY requirements.txt /app/requirements.txt
RUN pip3 install -v -r requirements.txt

EXPOSE 8000
CMD python run.py
