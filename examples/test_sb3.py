import gymnasium as gym
from gymnasium.wrappers.record_video import RecordVideo
import argparse
import sys

from stable_baselines3 import PPO, DQN, SAC, A2C, DDPG, TD3
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.monitor import Monitor

parser = argparse.ArgumentParser(description='Train an environment with an SB3 algorithm and then render 10 episodes.')
parser.add_argument('env', type=str, help='environment to test (e.g. CartPole-v1)')
parser.add_argument('-a', '--algo', type=str, default='PPO',
					help='algorithm to test from SB3, such as PPO (default), SAC, DQN... using default hyperparameters')
parser.add_argument('-n', '--nsteps', type=int, default=100_000, help='number of steps to train)')
parser.add_argument('-v', '--videorec', action="store_true", help='record and store video in a \"video\" directory, instead of using the screen)')

args = parser.parse_args()

str_env = args.env
str_algo = args.algo.upper()
algo = getattr(sys.modules[__name__], str_algo) # Obtains the classname based on the string
n_steps = args.nsteps
videorec = args.videorec

# Create environment
env = gym.make(str_env, render_mode=None)

print(f"Training {str_env} for {n_steps} steps with {str_algo}...")

# Instantiate the agent
model = algo('MlpPolicy', env=env, verbose=True)    

# Train the agent and display a progress bar
model.learn(total_timesteps=int(n_steps), progress_bar=True)

if not videorec:
	env = gym.make(str_env, render_mode="human")
else:
	env = gym.make(str_env, render_mode="rgb_array")
	trigger = lambda n: True
	env = RecordVideo(env, video_folder="./videos", episode_trigger=trigger, disable_logger=True)

env = Monitor(env)

# Evaluate the agent
n_episodes = 10
total_reward = 0
print(f"Evaluating for {n_episodes} episodes...")

for i in range(n_episodes): # episodes
	print(f"Executing episode {i}... ", end="")
	observation,_ = env.reset()
	episode_reward = 0
	while True:
		action, _states = model.predict(observation, deterministic=True)
		observation, reward, terminated, truncated, info = env.step(action)
		episode_reward += reward
		if terminated or truncated:
			print(f"reward: {episode_reward:.2f}")
			total_reward += episode_reward
			observation,_ = env.reset()
			break
env.close()

print(f"Mean reward: {total_reward/n_episodes:.2f}")
