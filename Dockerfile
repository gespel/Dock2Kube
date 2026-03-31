FROM python:3

EXPOSE 8080
EXPOSE 5000


ENTRYPOINT ["python3", "-c", "while True: print('Hello world!')"]
