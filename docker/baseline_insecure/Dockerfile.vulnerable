# Outdated Alpine base containing multiple known CVEs
FROM alpine:3.10

USER root

RUN apk update && apk add --no-cache curl python2 bash

WORKDIR /app
CMD ["/bin/sh"]
