import docker

client = docker.from_env()
client.images.build(path = ".", tag = "test:1.0.0")