FROM bash:latest

COPY . .

RUN apk update && apk add --no-cache curl

CMD ["echo", "asdasd"]