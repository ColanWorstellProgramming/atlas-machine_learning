#!/usr/bin/env python3
"""
Imports
"""
import numpy as np


def train(env, nb_episodes, alpha=0.000045, gamma=0.98, show_result=True):
    """
    Train With Animate
    """
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n
    weight = np.zeros((state_size, action_size))

    all_scores = []

    for episode in range(nb_episodes):
        state = env.reset()[None, :]
        done = False
        score = 0

        while not done:
            state_matrix = np.reshape(state, [1, -1])
            action, gradient = policy_gradient(state_matrix, weight)

            new_state, reward, done, _ = env.step(action)

            weight += alpha * gamma**episode * reward * gradient

            state = new_state
            score += reward

        print(f"Episode: {episode + 1}, Score: {score}", end="\r", flush=False)

        all_scores.append(score)

        if show_result and (episode + 1) % 1000 == 0:
            env.render(mode='human')

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
    gradient = state.T - np.sum(policy_probs * state.T, axis=1, keepdims=True)

    return action, gradient
