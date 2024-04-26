FROM bash:latest

COPY initScript.sh /

RUN apk update && apk add --no-cache curl

CMD ["bash", "/initScript.sh"]