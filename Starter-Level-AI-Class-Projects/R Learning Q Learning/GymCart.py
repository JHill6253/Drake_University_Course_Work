import gym

env = gym.make('MountainCar-v0')
env.reset()

for _ in range(100000):
    env.render()

    action = 2

    obv, reward, done, _ = env.step(action)
    print(obv)

env.close()
