# A Dockerfile that sets up a full Gymnasium, SB3 install with test dependencies
FROM ubuntu:20.04

ENV TZ=Europe/Madrid
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get -y update \
    && apt-get install --no-install-recommends -y \
    tzdata build-essential python3-dev libglu1-mesa-dev libgl1-mesa-dev libosmesa6-dev \
    xvfb unzip patchelf ffmpeg cmake swig nano python3.10 python3-pip python-is-python3\
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ARG USERNAME=rl
RUN useradd -m -s /bin/bash $USERNAME
USER $USERNAME
WORKDIR /home/$USERNAME

RUN pip install gymnasium[all]==0.29.1
RUN pip install stable-baselines3[extra]==2.2.1 rl-zoo3==2.2.1
RUN pip install mujoco==2.3.7
RUN pip uninstall -y mujoco-py

RUN mkdir /home/$USERNAME/examples
COPY examples /home/$USERNAME/examples

RUN mkdir /home/$USERNAME/my_scripts

