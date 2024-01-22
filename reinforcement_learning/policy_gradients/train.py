#!/usr/bin/env python3
"""
Imports
"""
import numpy as np


def train(env, nb_episodes, alpha=0.000045, gamma=0.98):
    """
    Train
    """
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n
    weight = np.zeros((state_size, action_size))
    all_scores = []

    for episode in range(nb_episodes):
        state = env.reset()[None, :]
        done = False
        score = 0
        gradients = []
        rewards = []

        while not done:
            state_matrix = np.reshape(state, [1, -1])
            action, gradient = policy_gradient(state_matrix, weight)

            new_state, reward, done, _ = env.step(action)

            weight += alpha * gamma**episode * reward * gradient

            gradients.append(gradient)
            rewards.append(reward)

            state = new_state
            score += reward

        rewards = np.array(rewards)

        for i in range(len(gradients)):
            learning = (alpha * gradients[i])
            discount = sum(gamma ** rewards[i:] * rewards[i:])
            weight += learning * discount

        print(f"Episode: {episode + 1}, Score: {score}")

        all_scores.append(score)

    return all_scores


def policy(matrix, weight):
    """
    Create Policy
    """
    z = np.dot(matrix, weight)
    exp_z = np.exp(z)
    policy = exp_z / np.sum(exp_z, axis=1, keepdims=True)

    return policy


def policy_gradient(state, weight):
    """
    Policy Gradient
    """
    policy_probs = policy(state, weight)
    action = np.random.choice(len(policy_probs[0]), p=policy_probs[0])

    s = policy_probs.reshape(-1, 1)

    soft = (np.diagflat(s) - np.dot(s, s.T))[action, :]

    log = soft / policy_probs[0, action]

    gradient = state.T.dot(log[None, :])

    return action, gradient
