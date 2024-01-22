#!/usr/bin/env python3
"""
Imports
"""
import numpy as np


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
