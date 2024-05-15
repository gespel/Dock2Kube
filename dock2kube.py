import uuid
import docker


class Dock2Kube:
    def __init__(self):
        self.client = docker.from_env()

    def build_image(self, path, version, name):
        (a, b) = self.client.images.build(path=path, tag=f"{name}:{version}")
        f = open(f"./{name}.tar", "wb")
        for c in a.save():
            f.write(c)
        f.close()


d2k = Dock2Kube()

path = input("Enter filepath (default = current folder): ")
if not path:
    path = "."

name = input("Enter a name (default = random uid): ")
if not name:
    name = uuid.uuid4()

version = input("Enter a version number (default = 1.0.0): ")
if not version:
    version = "1.0.0"


d2k.build_image(path=path, version=version, name=name)
