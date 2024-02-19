#!/usr/bin/env python3
"""
Imports
"""
import pandas as pd


def from_file(filename, delimiter):
    """
    Load data from file to a pandas dataframe
    """
    df = pd.read_csv(filename, delimiter=delimiter)

    return df
