#!/usr/bin/env python3
"""
Imports
"""
import numpy as np


def play(env, Q, max_steps=100):
    """
    play
    """
    total_reward = 0
    state, _ = env.reset()

    for _ in range(max_steps):
        action = np.argmax(Q[state, :])

        next_state, reward, done, _, _ = env.step(action)

        env.render()

        total_reward += reward
        state = next_state

        if done:
            break

    return total_reward
