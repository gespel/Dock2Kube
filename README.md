# Dock2Kube

Dock2Kube is a Python tool designed to create local Docker images ready for use with k3s Kubernetes from Dockerfiles.

## Overview

Dock2Kube simplifies the process of creating local Docker images tailored for k3s Kubernetes. It automates image building, tagging, and management, enabling faster development cycles and smoother integration with k3s deployments.

## Features

- **Efficient Image Building**: Quickly build Docker images from Dockerfiles.
- **Automatic Tagging**: Automatically tag images with versioning.
- **Seamless k3s Integration**: Easily manage and use images locally with k3s Kubernetes.

## Prerequisites

- Docker installed on your machine.
- Python 3.x installed.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/Dock2Kube.git
    ```

2. Navigate to the cloned directory:

    ```bash
    cd Dock2Kube
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Write your Dockerfile(s) for your application(s).

2. Run the `dock2kube.py` script:

    ```bash
    python dock2kube.py
    ```


3. The script will build the Docker image and tag it with a version based on the current date and time.

4. Start your k3s Kubernetes cluster and use the local images with your deployments.

## Example

Let's say you have a simple Dockerfile for a Node.js application:

```Dockerfile
# Dockerfile
FROM node:14-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

CMD ["npm", "start"]
```

To build this Dockerfile with Dock2Kube:

```bash

python dock2kube.py
```

This will build the image and tag it with a version.

## Contributing
Contributions are welcome! Feel free to submit issues and pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
