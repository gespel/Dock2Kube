import uuid
import docker
import pyfiglet
import os
import subprocess
import logging

class Dock2Kube:
    def __init__(self):
        print(pyfiglet.figlet_format("Dock2Kube", font="chunky", justify="center"))
        print("Made by Sten (Gespel) Heimbrodt\n\n")
        self.client = docker.from_env()
        self.logger = logging.getLogger("Dock2Kube")
        logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(name)s:%(levelname)s: %(message)s')

    def build_image(self, path, version, name):
        self.logger.info(f"Building image {name}:{version}...")
        (a, b) = self.client.images.build(path=path, tag=f"{name}:{version}")
        self.logger.info("Done!")

    def save_image(self, name, version, out_name):
        self.logger.info(f"Saving {name}:{version} to {out_name}...")
        a = self.client.images.get(f"{name}:{version}")

        f = open(out_name, "wb")
        for c in a.save():
            f.write(c)
        f.close()
        self.logger.info("Done!")

    def propagate_image(self, name):
        self.logger.info(f"Importing imagefile {name} to k3s...")
        proc = subprocess.Popen(f"sudo k3s ctr image import {name}", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        out, err = proc.communicate()
        if err is None:
            self.logger.info("Done!")
        else:
            self.logger.error(f"ERROR! {err}")



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
tar_name = f"{name}.tar"
print()

d2k.build_image(path=path, version=version, name=name)
d2k.save_image(name=name, version=version, out_name=tar_name)
d2k.propagate_image(tar_name)