import gymnasium as gym
from gymnasium.wrappers import RecordVideo


env = gym.make("CartPole-v1", render_mode="human")

observation, info = env.reset(seed=42)
for step_index in range(1000):
	action = env.action_space.sample()
	observation, reward, terminated, truncated, info = env.step(action)

	if terminated or truncated:
		observation, info = env.reset()


env.close()
