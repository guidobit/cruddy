ARG ALPINE_VERSION=3.6
FROM alpine:${ALPINE_VERSION}


LABEL name="MongoDB in Alpine ${ALPINE_VERSION}" \
      vendor="Bloq"

USER root
RUN apk add --no-cache --update-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
        su-exec=0.2-r0 && \
    apk add mongodb && \
    rm /usr/bin/mongoperf

EXPOSE 27017/tcp
CMD [ "mongod", "--bind_ip", "0.0.0.0" ]
