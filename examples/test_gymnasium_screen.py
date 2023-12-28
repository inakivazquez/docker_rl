import gymnasium as gym
import sys

if len(sys.argv) < 2:
	print(f"Use: {sys.argv[0]} env [n_steps]")
	print(f"Example: {sys.argv[0]} CartPole-v1")
	print(f"Example: {sys.argv[0]} CartPole-v1 200000")
	quit()

str_env = sys.argv[1]
if len(sys.argv) > 2:
	n_steps = int(sys.argv[2])
else:
	n_steps = 1_000

env = gym.make(str_env, render_mode="human")

observation, info = env.reset(seed=42)
for step_index in range(n_steps):
	action = env.action_space.sample()
	observation, reward, terminated, truncated, info = env.step(action)

	if terminated or truncated:
		observation, info = env.reset()


env.close()
