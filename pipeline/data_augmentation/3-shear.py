"""
Imports
"""
import tensorflow as tf


def shear_image(image, intensity):
    """
    Shear image
    """
    tf.keras.preprocessing.image.random_shear(image,
                                              intensity,
                                              row_axis=1,
                                              col_axis=0,
                                              channel_axis=2)
