"""
Imports
"""
import tensorflow as tf


def crop_image(image, size):
    """
    Crop image based on size
    """
    return tf.image.random_crop(image, size)
