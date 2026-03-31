FROM python:3
FROM node:18

ENTRYPOINT ["python3", "-c", "while True: print('Hello world!')"]
