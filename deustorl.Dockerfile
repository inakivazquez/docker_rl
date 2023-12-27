# A Dockerfile that sets up a full Gymnasium, SB3 install with test dependencies
ARG PYTHON_VERSION=3.10
FROM python:$PYTHON_VERSION

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get -y update \
    && apt-get install --no-install-recommends -y \
    libglu1-mesa-dev libgl1-mesa-dev libosmesa6-dev \
    xvfb unzip patchelf ffmpeg cmake swig nano \
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

RUN mkdir /home/$USERNAME/examples
COPY examples /home/$USERNAME/examples

RUN mkdir /home/$USERNAME/my_scripts

