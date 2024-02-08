"""
Imports
"""
import tensorflow as tf


def change_brightness(image, max_delta):
    """
    Change brightness
    """
    return tf.image.random_brightness(image, max_delta)
