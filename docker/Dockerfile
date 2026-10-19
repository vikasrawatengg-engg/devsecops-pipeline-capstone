# Modern, actively patched base image with unprivileged execution
FROM alpine:3.20

RUN addgroup -S appgroup && adduser -S appuser -G appgroup
RUN apk update && apk upgrade --no-cache && apk add --no-cache ca-certificates

USER appuser
WORKDIR /home/appuser
CMD ["/bin/sh"]
