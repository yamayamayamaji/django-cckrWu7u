FROM mcr.microsoft.com/devcontainers/python:3.12-bullseye

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    curl \
    pkg-config libxmlsec1-dev libxmlsec1-openssl clang \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

ENTRYPOINT /bin/bash /entrypoint.sh
