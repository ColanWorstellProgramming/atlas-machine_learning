#!/usr/bin/env python3
"""
Imports
"""
import numpy as np


def epsilon_greedy(Q, state, epsilon):
    """
    epsilon greedy
    """
    if np.random.uniform(0, 1) < epsilon:
        next_action = np.random.randint(0, Q.shape[1])
    else:
        next_action = np.argmax(Q[state, :])

    return next_action
