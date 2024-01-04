#!/usr/bin/env python3
"""
Imports
"""
import numpy as np


def train(env, Q, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99, epsilon=1, min_epsilon=0.1, epsilon_decay=0.05):
    """
    Train
    """
    total_rewards = []

    for _ in range(episodes):
        state, _ = env.reset()
        episode_reward = 0

        for _ in range(max_steps):
            if np.random.rand() < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(Q[state, :])

            next_state, reward, done, _, _ = env.step(action)

            Q[state, action] = Q[state, action] + (1 - alpha) * (reward + gamma * np.max(Q[next_state, :]) - Q[state, action])

            episode_reward += reward
            state = next_state

            if done and reward == 0:
                Q[state, action] = -1

            if done:
                break

        total_rewards.append(episode_reward)

        epsilon = max(min_epsilon, epsilon - epsilon_decay)

    return Q, total_rewards


def epsilon_greedy(Q, state, epsilon):
    """
    epsilon greedy
    """
    if np.random.uniform(0, 1) < epsilon:
        next_action = np.random.randint(0, Q.shape[1])
    else:
        next_action = np.argmax(Q[state, :])

    return next_action
