import gymnasium as gym
from gymnasium.wrappers import RecordVideo

env = gym.make("Ant-v4", render_mode="rgb_array_list")

trigger = lambda t: True
env = RecordVideo(env, video_folder="./videos", episode_trigger=trigger, disable_logger=True)

observation, info = env.reset(seed=42)
for step_index in range(1000):
	action = env.action_space.sample()
	observation, reward, terminated, truncated, info = env.step(action)

	if terminated or truncated:
		observation, info = env.reset()


env.close()
