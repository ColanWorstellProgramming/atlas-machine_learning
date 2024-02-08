#!/usr/bin/env python3
"""
Imports
"""
import tensorflow as tf


def flip_image(image):
    """
    Flip image
    """
    return tf.image.flip_left_right(image)
