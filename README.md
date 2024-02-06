# Docker containers for Reinforcement Learning experimentation

<p align="center">
  <img src="https://github.com/inakivazquez/docker_rl/assets/47280218/d344da8c-19e4-4271-befa-b59b87dd503f" width="200" height="200"/>
</p>

This repository contains the necessary files to create docker containers for experimenting with [Gymnasium](https://gymnasium.farama.org/) and [Stable-Baselines3](https://stable-baselines3.readthedocs.io/).

The containers can be executed in Linux and Windows (either directly of using [WSL2](https://learn.microsoft.com/en-us/windows/wsl/about#what-is-wsl-2)). 

### Features support

| Feature  | Linux/WSL2 | Windows |
| ------------- | :-------------: | :-------------: |
| GPU CUDA support | :heavy_check_mark: | :heavy_check_mark: |
| Interactive visualization | :heavy_check_mark: 
| Video recording | :heavy_check_mark: | :heavy_check_mark: | 
| Classic control environments | :heavy_check_mark: | :heavy_check_mark: | 
| Box2D environments | :heavy_check_mark: | :heavy_check_mark: | 
| ToyText environments | :heavy_check_mark: | :heavy_check_mark:| 
| MuJoCo environments | :heavy_check_mark:
| Atari environments | :heavy_check_mark: | :heavy_check_mark: | 


## Basic instructions
The following instructions are for easily creating and using containers with `docker compose`:
1. Select a working directory for your project in your host computer (e.g. `rl-scripts`) and move there. This directory will be mapped inside the container in the path `/home/rl/my_scripts`.
2. Download in that directory the `compose.yaml` file from github.

3. Execute one of the below options, depending on your system, to create the container (default name is `rltrain`). It may be necessary to use `sudo` preceding the docker commands in Linux.  
> [!NOTE]
> It may take some minutes to download the image the first time.

   * Starting the Linux/WSL2 CPU-only container:
     ```
     docker compose up linux-cpu -d
     ```

   * Starting the Linux/WSL2 GPU-enabled container:
     ```
     docker compose up linux-gpu -d
     ```

   * Starting the Windows CPU-only container:
     ```
     docker compose up windows-cpu -d
     ```

   * Starting the Windows GPU-enabled container:
     ```
     docker compose up windows-gpu -d
     ```
> [!WARNING]
> Do not forget the final `-d`

4. Open a terminal session on the container `rltrain` (multiple terminal sessions maybe opened on the same container for starting tensorboard or parallel trainings):
   ```
   docker exec -it rltrain /bin/bash
   ```

5. For stopping the container after working with it:
   ```
   docker stop rltrain
   ```

6. To start the container again, just execute the previous `docker compose up` command, or:
   ```
   docker start rltrain
   ```
   


### Starting Tensorboard
In a different terminal session on the container, type:
```
tensorboard --logdir logs --bind_all
```

### Directory structure and example scripts
The container provides the following directory structure:

```
── /home/rl/
   ├── examples
   │   ├── check_cuda.py
   │   ├── test_gymnasium.py
   │   └── test_sb3.py
   └── my_scripts
```

* `my_scripts`: this is where the working directory of the host is mapped. Your python scripts and experiments should be here.
* `examples`: some example scripts are provided here, to check basic functionality
   * `check_cuda.py`: checks that CUDA is properly configured and displays the number of GPUs available.
   * `test_gymnasium.py`: launches a Gymnasium environment passed as parameter (`--help` for detailed parameters information).
   * `test_sb3.py`: launches a Stable-Baselines3 training with a Gymnasium environment (`--help` for detailed parameters information).

**Example**: launch a Gymnasium test in interactive mode
```
python test_gymnasium.py --env LunarLander-v2 -n 100000
```
**Example**: launch a Gymnasium test and record the episodes videos (a `videos` directory will be created in the working directory).
```
python test_gymnasium.py --env Ant-v4 -n 100000 -r
```
>[!WARNING]
>Note: as Ant-v4 is based on MuJoCo, this environment is not supported in the Windows-based container.

**Example**: launch a SB3 training interactively and log progress in tensorboard (a `logs` directory will be created in the working directory):
```
python test_sb3.py --env LunarLander-v2 --algo ppo -n 200000 -t
```

> [!NOTE]
> For videos and tensoboard logs, the `videos` and `logs` directories are created in the working directory, therefore for the above examples, in order to be able to access`videos` and `logs` from the host computer, those directories should be generated under the `my_scripts` (which is mapped on the host). That can be easily done by invoking the example scripts from the `my_scripts` directory:
```console
rl@foobar:/home/rl/my_scripts$ python ../examples/test_sb3.py --env LunarLander-v2 --algo ppo -n 200000 -t
```

## Appendix: Additional instructions for further hacking and customization

### Build the image from the GitHub repository
```
docker build -f rl-base.Dockerfile -t inakivazquez/rl-base:latest .
```

### Direct installation without docker compose
This example is for CUDA + MuJoCo support in Linux/WSL2 using network mode host:
```
docker pull inakivazquez/rl-base
docker container create --name rltrain --privileged --network host -it --gpus all -v .:/home/rl/my_scripts -e DISPLAY=$DISPLAY -e SDL_VIDEODRIVER=x11 -v /tmp/.X11-unix:/tmp/.X11-unix inakivazquez/rl-base
docker start rltrain
docker exec -it rltrain /bin/bash
```
### Full features in Windows via WSL2:
Follow the instructions at the [Ubuntu tutorial for WSL2](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#1-overview), basically: 
1. Install WSL for Windows 10 / 11
1. Install Ubuntu over WSL:
```
wsl --install Ubuntu
```

### GPU CUDA installation instructions:
Follow the official instructions at [NVIDIA website](https://developer.nvidia.com/cuda-12-1-0-download-archive).
