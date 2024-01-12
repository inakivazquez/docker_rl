# Docker containers for Reinforcement Learning experimentation
This repository contains the necessary files to create docker containers for experimenting with [Gymnasium](https://gymnasium.farama.org/) and [Stable-Baselines3](https://stable-baselines3.readthedocs.io/).

The containers can be executed in Linux and Windows (either directly of using [WSL2](https://learn.microsoft.com/en-us/windows/wsl/about#what-is-wsl-2)). 

### Features support

| Feature  | Linux/WSL2 | Windows |
| ------------- | :-------------: | :-------------: |
| GPU CUDA support  | X | X |
| Interactive visualization	| X 
| Video recording			    | X | X | 
| Classic control environments | X | X | 
| Box2D environments | X | X | 
| ToyText environments | X	|     X| 
| MuJoCo environments | X
| Atari environments | X | X | 


## Basic instructions
The following instructions are for easily creating and using containers with `docker compose`:
1. Create a `rl` directory and move there
2. Download in that directory the `compose.yaml` file from github

3. Execute one of the below options, depending on your system (it may be necessary to use `sudo` preceding the docker commands).
   Note that it may take some minutes to download the image the first time. Do not forget the final `-d`

   * Starting the Linux/WSL2 CPU-only container:
`docker compose up linux-cpu -d`

   * Starting the Linux/WSL2 GPU-enabled container:
`docker compose up linux-gpu -d`

   * Starting the Windows CPU-only container:
`docker compose up windows-cpu -d`

   * Starting the Windows GPU-enabled container:
`docker compose up windows-gpu -d`

5. Open a terminal session over the container (multiple terminal sessions maybe opened on the same container for starting tensorboard or parallel trainings):
`docker exec -it rltrain /bin/bash`

6. For stopping the container after working with it
`docker stop rltrain`

7. To start the container again, just execute the previous `docker compose up` command.


### Starting Tensorboard:
`tensorboard --logdir logs --bind_all`


## Appendix: Additional instructions for further customization

### Build the image from the GitHub repository
`docker build -f deustorl-base3.Dockerfile -t inakivazquez/deustorl:base3 .`

### Direct installation without docker compose
This example is for GPU + Mujoco support in Linux/WSL using network mode host:
```
docker pull inakivazquez/deustorl:base3
docker container create --name rltrain --privileged --network host -it --gpus all -v .:/home/rl/my_scripts -e DISPLAY=$DISPLAY -e SDL_VIDEODRIVER=x11 -v /tmp/.X11-unix:/tmp/.X11-unix inakivazquez/deustorl:base3
docker start rltrain
docker exec -it rltrain /bin/bash
```
### Interactive support in WINDOWS via WSL2:
Follow the instructions at the [Ubuntu tutorial for WSL2](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#1-overview), basically: 
1. Install WSL for Windows 11
1. Install Ubuntu over WSL: `wsl --install Ubuntu`

### GPU CUDA installation instructions:
Follow the official instructions at [NVIDIA website](https://developer.nvidia.com/cuda-11-8-0-download-archive)
