import gymnasium as gym

from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy

# Create environment
env = gym.make("LunarLander-v2", render_mode="rgb_array")

# Instantiate the agent
model = PPO(policy="MlpPolicy", env=env, n_steps=1024, batch_size=64, n_epochs=4, gamma=0.999, gae_lambda=0.98, ent_coef=0.01, verbose=True)

# Train the agent and display a progress bar
model.learn(total_timesteps=int(2e5), progress_bar=True)

# Evaluate the agent
mean_reward, std_reward = evaluate_policy(model, model.get_env(), n_eval_episodes=10)
print ("Mean reward: ", mean_reward)

# Enjoy trained agent

env = gym.make("LunarLander-v2", render_mode="human")
for i in range(10): # episodes
	print(f"Executing episode {i}...")
	observation,_ = env.reset()
	while True:
		action, _states = model.predict(observation, deterministic=True)
		observation, reward, terminated, truncated, info = env.step(action)
		if terminated or truncated:
			observation,_ = env.reset()
			break
env.close()
