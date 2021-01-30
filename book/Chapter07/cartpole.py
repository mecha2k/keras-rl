import gym
import numpy as np

env = gym.make("CartPole-v0")
HighReward = 0
BestWeights = None

for i in range(200):
    observation = env.reset()
    Weights = np.random.uniform(-1, 1, 4)
    SumReward = 0
    for j in range(1000):
        env.render()
        action = 0 if np.matmul(Weights, observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        SumReward += reward
        if done:
            break
    if SumReward > HighReward:
        HighReward = SumReward
        BestWeights = Weights
    if i % 10 == 0:
        print(i, Weights, observation, action, SumReward, BestWeights)

observation = env.reset()
for j in range(1000):
    env.render()
    action = 0 if np.matmul(BestWeights, observation) < 0 else 1
    observation, reward, done, info = env.step(action)
    if j % 20 == 0:
        print(j, action)
