import uuid
import docker


class Dock2Kube:
    def __init__(self):
        pass

    def buildImage(self, path, version, name):
        client = docker.from_env()
        (a, b) = client.images.build(path=path, tag=f"{name}:{version}")
        f = open(f"./{name}.tar", "wb")
        for c in a.save():
            f.write(c)
        f.close()


d2k = Dock2Kube()

path = input("Enter filepath (default = current folder): ")
if not path:
    path = "."

version = input("Enter a version number (default = 1.0.0): ")
if not version:
    version = "1.0.0"

name = input("Enter a name (default = random uid): ")
if not name:
    name = uuid.UUID()

d2k.buildImage(path=path, version=version, name=name)
