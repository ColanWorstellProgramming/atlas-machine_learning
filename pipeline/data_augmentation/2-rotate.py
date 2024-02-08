"""
Imports
"""
import tensorflow as tf


def rotate_image(image):
    """
    Rotate image
    """
    return tf.image.rot90(image)
