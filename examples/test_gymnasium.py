import gymnasium as gym
from gymnasium.wrappers.record_video import RecordVideo
import argparse

parser = argparse.ArgumentParser(description='Test Gymnasium environments with random actions.')
parser.add_argument('env', type=str, help='environment to test (e.g. CartPole-v1)')
parser.add_argument('-n', '--nsteps', type=int, default=1_000, help='number of steps to execute)')
parser.add_argument('-v', '--videorec', action="store_true", help='record and store video in a \"video\" directory, instead of using the screen)')

args = parser.parse_args()

str_env = args.env
n_steps = args.nsteps
videorec = args.videorec

if not videorec:
	env = gym.make(str_env, render_mode="human")
else:
	env = gym.make(str_env, render_mode="rgb_array")
	trigger = lambda n: True
	env = RecordVideo(env, video_folder="./videos", episode_trigger=trigger, disable_logger=True)

observation, info = env.reset(seed=42)
for step_index in range(n_steps):
	action = env.action_space.sample()
	observation, reward, terminated, truncated, info = env.step(action)

	if terminated or truncated:
		observation, info = env.reset()


env.close()
